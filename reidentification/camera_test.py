"""
Real-Time Camera Test and Person Re-Identification Demo
Run this with: .venv312\Scripts\python.exe camera_test.py
"""

import cv2
import numpy as np

def test_camera():
    """Test if camera works and show live feed"""
    print("Testing camera...")
    
    # Try different camera indices
    camera_idx = None
    for idx in [0, 1, 2]:
        cap = cv2.VideoCapture(idx, cv2.CAP_DSHOW)  # DirectShow for Windows
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"✅ Camera {idx} works! Resolution: {frame.shape[1]}x{frame.shape[0]}")
                camera_idx = idx
                cap.release()
                break
        cap.release()
        print(f"❌ Camera {idx} not available")
    
    if camera_idx is None:
        print("\n⚠️ No camera found!")
        print("Please check:")
        print("1. Is your camera connected?")
        print("2. Is another app using the camera? (Close Zoom, Teams, etc.)")
        print("3. Check Windows Settings > Privacy > Camera")
        return None
    
    return camera_idx

def run_camera_demo():
    """Run live camera demo"""
    camera_idx = test_camera()
    if camera_idx is None:
        return
    
    print(f"\nOpening camera {camera_idx}...")
    print("Press 'q' to quit")
    print("Press 's' to save a screenshot")
    
    cap = cv2.VideoCapture(camera_idx, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    screenshot_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame")
            break
        
        # Add text overlay
        cv2.putText(frame, "Person Re-ID Camera Demo", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, "Press 'q' to quit, 's' to screenshot", (10, 60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        cv2.imshow("Camera Feed - Person Re-ID", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Quitting...")
            break
        elif key == ord('s'):
            filename = f"screenshot_{screenshot_count}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Saved: {filename}")
            screenshot_count += 1
    
    cap.release()
    cv2.destroyAllWindows()
    print("Camera closed.")

if __name__ == "__main__":
    run_camera_demo()
