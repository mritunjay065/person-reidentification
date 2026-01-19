"""
Robust Person Re-ID Demo using OpenCV's SFace Model
Handles different poses, expressions, and lighting conditions

Run: python realtime_reid_robust.py
"""

import cv2
import numpy as np
import os
import urllib.request
import pickle

print("="*60)
print("  Setting up Face Recognition Models...")
print("="*60)

# Model paths
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "face_models")
os.makedirs(MODEL_DIR, exist_ok=True)

# Face detection model (YuNet)
FACE_DETECT_MODEL = os.path.join(MODEL_DIR, "face_detection_yunet_2023mar.onnx")
FACE_DETECT_URL = "https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx"

# Face recognition model (SFace)
FACE_RECOG_MODEL = os.path.join(MODEL_DIR, "face_recognition_sface_2021dec.onnx")
FACE_RECOG_URL = "https://github.com/opencv/opencv_zoo/raw/main/models/face_recognition_sface/face_recognition_sface_2021dec.onnx"

def download_model(url, path):
    """Download model if not exists"""
    if not os.path.exists(path):
        print(f"Downloading: {os.path.basename(path)}...")
        try:
            urllib.request.urlretrieve(url, path)
            print(f"✅ Downloaded: {os.path.basename(path)}")
        except Exception as e:
            print(f"❌ Failed to download: {e}")
            return False
    else:
        print(f"✅ Found: {os.path.basename(path)}")
    return True

# Download models
if not download_model(FACE_DETECT_URL, FACE_DETECT_MODEL):
    print("Please download manually from:")
    print(FACE_DETECT_URL)
    exit(1)

if not download_model(FACE_RECOG_URL, FACE_RECOG_MODEL):
    print("Please download manually from:")
    print(FACE_RECOG_URL)
    exit(1)

class RobustFaceReID:
    def __init__(self):
        print("\nInitializing face recognition...")
        
        # Initialize face detector (YuNet)
        self.detector = cv2.FaceDetectorYN.create(
            FACE_DETECT_MODEL,
            "",
            (320, 320),
            0.9,  # Score threshold
            0.3,  # NMS threshold
            5000  # Top K
        )
        
        # Initialize face recognizer (SFace)
        self.recognizer = cv2.FaceRecognizerSF.create(
            FACE_RECOG_MODEL,
            ""
        )
        
        self.gallery = {}  # name -> list of feature vectors
        self.gallery_images = {}  # name -> image
        self.cosine_threshold = 0.363  # SFace recommended threshold
        self.l2_threshold = 1.128
        self.gallery_file = os.path.join(MODEL_DIR, "gallery.pkl")
        
        # Load saved gallery if exists
        self.load_gallery()
        
        print("✅ Models loaded successfully!")
    
    def save_gallery(self):
        """Save gallery to file"""
        data = {
            'gallery': self.gallery,
            'gallery_images': self.gallery_images
        }
        with open(self.gallery_file, 'wb') as f:
            pickle.dump(data, f)
        print(f"💾 Gallery saved! ({len(self.gallery)} persons)")
    
    def load_gallery(self):
        """Load gallery from file"""
        if os.path.exists(self.gallery_file):
            try:
                with open(self.gallery_file, 'rb') as f:
                    data = pickle.load(f)
                self.gallery = data.get('gallery', {})
                self.gallery_images = data.get('gallery_images', {})
                print(f"📂 Loaded saved gallery: {len(self.gallery)} persons")
            except Exception as e:
                print(f"⚠️ Could not load gallery: {e}")
    
    def detect_face(self, image):
        """Detect face and return bounding box"""
        h, w = image.shape[:2]
        self.detector.setInputSize((w, h))
        
        _, faces = self.detector.detect(image)
        
        if faces is not None and len(faces) > 0:
            # Get largest face
            largest_face = max(faces, key=lambda f: f[2] * f[3])
            return largest_face
        return None
    
    def extract_features(self, image, face):
        """Extract 128-dim face features using SFace"""
        aligned_face = self.recognizer.alignCrop(image, face)
        features = self.recognizer.feature(aligned_face)
        return features
    
    def register_person(self, name, image):
        """Register a person with multiple feature vectors for robustness"""
        face = self.detect_face(image)
        
        if face is None:
            print(f"❌ No face detected for {name}")
            return False, None
        
        features = self.extract_features(image, face)
        
        # Store multiple embeddings per person for better matching
        if name not in self.gallery:
            self.gallery[name] = []
        
        self.gallery[name].append(features)
        
        # Store image thumbnail
        x, y, w, h = int(face[0]), int(face[1]), int(face[2]), int(face[3])
        face_img = image[max(0,y):y+h, max(0,x):x+w]
        if face_img.size > 0:
            self.gallery_images[name] = cv2.resize(face_img, (80, 100))
        
        num_samples = len(self.gallery[name])
        print(f"✅ Registered: {name} (samples: {num_samples})")
        
        bbox = (x, y, w, h)
        return True, bbox
    
    def identify_person(self, image):
        """Identify person using cosine similarity"""
        face = self.detect_face(image)
        
        if face is None:
            return None, 0.0, {}, None
        
        features = self.extract_features(image, face)
        
        all_scores = {}
        best_match = None
        best_score = -1
        
        for name, feature_list in self.gallery.items():
            # Compare against all stored embeddings and take the best match
            max_score = -1
            for stored_features in feature_list:
                # Cosine similarity
                score = self.recognizer.match(features, stored_features, cv2.FaceRecognizerSF_FR_COSINE)
                if score > max_score:
                    max_score = score
            
            all_scores[name] = max_score
            
            if max_score > best_score:
                best_score = max_score
                best_match = name
        
        x, y, w, h = int(face[0]), int(face[1]), int(face[2]), int(face[3])
        bbox = (x, y, w, h)
        
        if best_score >= self.cosine_threshold:
            return best_match, best_score, all_scores, bbox
        
        return None, best_score, all_scores, bbox
    
    def run(self):
        """Run the demo"""
        print("\n" + "="*60)
        print("  🎯 ROBUST Person Re-ID Demo (OpenCV SFace)")
        print("="*60)
        print("\nThis model can recognize faces with:")
        print("  ✓ Different expressions")
        print("  ✓ Different angles/poses")
        print("  ✓ Different lighting")
        print("  ✓ With/without glasses")
        print("\nControls:")
        print("  1-9 : Register person (press multiple times for better accuracy)")
        print("  r   : Toggle Re-ID mode")
        print("  d   : Toggle debug scores")
        print("  c   : Clear gallery")
        print("  +/- : Adjust threshold")
        print("  s   : Save gallery")
        print("  q   : Quit")
        print("="*60)
        print("\nTIP: Register each person 2-3 times with different expressions!")
        print("="*60 + "\n")
        
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        if not cap.isOpened():
            print("❌ Cannot open camera")
            return
        
        print("✅ Camera opened!")
        
        reid_mode = False
        debug_mode = True
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            display = frame.copy()
            
            # Header background
            cv2.rectangle(display, (0, 0), (640, 90), (40, 40, 40), -1)
            cv2.putText(display, "Robust Face Re-ID (SFace)", (10, 25),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.putText(display, f"Threshold: {self.cosine_threshold:.3f} | Gallery: {len(self.gallery)} persons", 
                       (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)
            
            # Count total samples
            total_samples = sum(len(v) for v in self.gallery.values())
            cv2.putText(display, f"Total samples: {total_samples} | 1-9:Add | r:ReID | c:Clear | q:Quit", 
                       (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)
            
            if reid_mode:
                cv2.putText(display, "RE-ID: ON", (545, 25),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
                
                name, score, all_scores, bbox = self.identify_person(frame)
                
                # Draw face bounding box
                if bbox is not None:
                    x, y, w, h = bbox
                    color = (0, 255, 0) if name else (0, 0, 255)
                    cv2.rectangle(display, (x, y), (x+w, y+h), color, 3)
                    
                    # Show name above face
                    if name:
                        label = f"{name}: {score:.3f}"
                        cv2.putText(display, label, (x, y-10),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    else:
                        cv2.putText(display, f"Unknown: {score:.3f}", (x, y-10),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                
                # Debug scores panel
                if debug_mode and all_scores:
                    y_pos = 110
                    cv2.rectangle(display, (5, 95), (200, 95 + 25 + len(all_scores) * 22), (30, 30, 30), -1)
                    cv2.putText(display, "Cosine Scores:", (10, y_pos),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 0), 1)
                    for pname, sim in sorted(all_scores.items(), key=lambda x: x[1], reverse=True):
                        y_pos += 22
                        is_match = sim >= self.cosine_threshold
                        color = (0, 255, 0) if is_match else (100, 100, 255)
                        marker = "✓" if is_match else "✗"
                        samples = len(self.gallery.get(pname, []))
                        cv2.putText(display, f"{marker} {pname}: {sim:.4f} ({samples})", (15, y_pos),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
                
                # Result display
                if name:
                    cv2.putText(display, f"MATCH: {name}", (400, 50),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                elif bbox:
                    cv2.putText(display, "UNKNOWN", (480, 50),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                else:
                    cv2.putText(display, "NO FACE", (480, 50),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (128, 128, 128), 2)
            else:
                cv2.putText(display, "REGISTRATION", (450, 25),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
                
                # Show detected face during registration
                face = self.detect_face(frame)
                if face is not None:
                    x, y, w, h = int(face[0]), int(face[1]), int(face[2]), int(face[3])
                    cv2.rectangle(display, (x, y), (x+w, y+h), (255, 255, 0), 2)
                    cv2.putText(display, "Face detected - Press 1-9 to register", (x, y-10),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)
            
            # Gallery thumbnails at bottom
            x_offset = 10
            for name, img in self.gallery_images.items():
                thumb = cv2.resize(img, (50, 65))
                y_start = 405
                if x_offset + 50 < 630:
                    try:
                        display[y_start:y_start+65, x_offset:x_offset+50] = thumb
                        samples = len(self.gallery.get(name, []))
                        cv2.putText(display, f"{name[-1]}({samples})", (x_offset, y_start+78),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)
                    except:
                        pass
                x_offset += 60
            
            cv2.imshow("Robust Face Re-ID", display)
            
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q'):
                break
            elif key == ord('r'):
                reid_mode = not reid_mode
                print(f"Re-ID mode: {'ON' if reid_mode else 'OFF'}")
            elif key == ord('d'):
                debug_mode = not debug_mode
            elif key == ord('c'):
                self.gallery.clear()
                self.gallery_images.clear()
                print("Gallery cleared")
            elif key == ord('s'):
                self.save_gallery()
            elif key == ord('+') or key == ord('='):
                self.cosine_threshold = min(1.0, self.cosine_threshold + 0.02)
                print(f"Threshold: {self.cosine_threshold:.3f}")
            elif key == ord('-'):
                self.cosine_threshold = max(0.1, self.cosine_threshold - 0.02)
                print(f"Threshold: {self.cosine_threshold:.3f}")
            elif ord('1') <= key <= ord('9'):
                person_name = f"Person_{chr(key)}"
                success, bbox = self.register_person(person_name, frame)
                if success and bbox:
                    x, y, w, h = bbox
                    cv2.rectangle(display, (x, y), (x+w, y+h), (0, 255, 0), 3)
                    cv2.putText(display, f"Registered: {person_name}", (x, y-10),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.imshow("Robust Face Re-ID", display)
                    cv2.waitKey(500)
        
        cap.release()
        cv2.destroyAllWindows()
        print("\n✅ Demo closed")

if __name__ == "__main__":
    demo = RobustFaceReID()
    demo.run()
