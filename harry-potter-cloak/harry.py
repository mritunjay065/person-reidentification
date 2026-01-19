"""
🧙 Harry Potter Invisible Cloak
================================
Step 1: Capture background (stay out of frame)
Step 2: Click on cloth to capture its color
Step 3: Wear the cloth - it becomes invisible!

Run: python harry.py
"""

import cv2
import numpy as np
import time

# Global variables for mouse callback
clicked_color = None
click_pos = None

def mouse_callback(event, x, y, flags, param):
    """Handle mouse clicks to sample color"""
    global clicked_color, click_pos
    if event == cv2.EVENT_LBUTTONDOWN:
        click_pos = (x, y)

def main():
    global clicked_color, click_pos
    
    print("\n" + "="*50)
    print("  🧙 HARRY POTTER INVISIBLE CLOAK 🧙")
    print("="*50)
    
    # Open camera
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    if not cap.isOpened():
        print("❌ Cannot open camera!")
        return
    
    cv2.namedWindow("Invisible Cloak")
    cv2.setMouseCallback("Invisible Cloak", mouse_callback)
    
    background = None
    cloak_hue = None
    hue_tolerance = 20  # Increased default tolerance for better coverage
    
    # ============ STEP 1: CAPTURE BACKGROUND ============
    print("\n📸 STEP 1: CAPTURING BACKGROUND...")
    print("   ⚠️  STAY OUT OF THE FRAME!")
    print("   Capturing in 3 seconds...")
    
    # Countdown
    start_time = time.time()
    while time.time() - start_time < 3:
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.flip(frame, 1)
        
        remaining = 3 - int(time.time() - start_time)
        cv2.rectangle(frame, (0, 0), (640, 100), (0, 0, 150), -1)
        cv2.putText(frame, f"STEP 1: STAY OUT OF FRAME!", (80, 40),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
        cv2.putText(frame, f"Capturing background in {remaining}...", (120, 75),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.imshow("Invisible Cloak", frame)
        cv2.waitKey(1)
    
    # Capture background frames
    print("   Capturing background...")
    frames = []
    for i in range(30):
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            frames.append(frame)
            cv2.rectangle(frame, (0, 0), (640, 60), (0, 150, 0), -1)
            cv2.putText(frame, f"Capturing background... {i+1}/30", (150, 40),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            cv2.imshow("Invisible Cloak", frame)
            cv2.waitKey(30)
    
    if frames:
        background = np.median(frames, axis=0).astype(np.uint8)
        print("   ✅ Background captured!")
    else:
        print("   ❌ Failed to capture background!")
        return
    
    # ============ STEP 2: CAPTURE CLOTH COLOR ============
    print("\n🎨 STEP 2: CLICK ON YOUR CLOTH TO CAPTURE ITS COLOR")
    print("   📍 Hold the cloth in the GREEN BOX area")
    print("   👆 Click anywhere on the cloth")
    
    while cloak_hue is None:
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.flip(frame, 1)
        
        # Draw big targeting box in center
        h, w = frame.shape[:2]
        box_w, box_h = 250, 250
        box_x = (w - box_w) // 2
        box_y = (h - box_h) // 2
        
        # Draw green targeting box
        cv2.rectangle(frame, (box_x, box_y), (box_x + box_w, box_y + box_h), (0, 255, 0), 3)
        cv2.rectangle(frame, (box_x - 5, box_y - 5), (box_x + box_w + 5, box_y + box_h + 5), (0, 200, 0), 1)
        
        # Draw crosshair
        cx, cy = w // 2, h // 2
        cv2.line(frame, (cx - 30, cy), (cx + 30, cy), (0, 255, 0), 2)
        cv2.line(frame, (cx, cy - 30), (cx, cy + 30), (0, 255, 0), 2)
        cv2.circle(frame, (cx, cy), 50, (0, 255, 0), 2)
        
        # Draw instruction
        cv2.rectangle(frame, (0, 0), (640, 100), (150, 100, 0), -1)
        cv2.putText(frame, "STEP 2: CAPTURE CLOTH COLOR", (130, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, "1. Hold cloth in GREEN BOX", (180, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
        cv2.putText(frame, "2. CLICK on the cloth", (200, 85),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
        
        # Check for click
        if click_pos is not None:
            x, y = click_pos
            if 0 <= x < frame.shape[1] and 0 <= y < frame.shape[0]:
                # Show click feedback
                cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)
                cv2.imshow("Invisible Cloak", frame)
                cv2.waitKey(200)
                
                # Sample color from clicked area (10x10 region)
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                region = hsv[max(0,y-10):y+10, max(0,x-10):x+10]
                if region.size > 0:
                    cloak_hue = int(np.median(region[:,:,0]))
                    sat = int(np.median(region[:,:,1]))
                    val = int(np.median(region[:,:,2]))
                    
                    # Get color name
                    if cloak_hue < 10 or cloak_hue > 170:
                        color_name = "RED"
                        color_bgr = (0, 0, 255)
                    elif 10 <= cloak_hue < 25:
                        color_name = "ORANGE"
                        color_bgr = (0, 165, 255)
                    elif 25 <= cloak_hue < 35:
                        color_name = "YELLOW"
                        color_bgr = (0, 255, 255)
                    elif 35 <= cloak_hue < 85:
                        color_name = "GREEN"
                        color_bgr = (0, 255, 0)
                    elif 85 <= cloak_hue < 130:
                        color_name = "BLUE"
                        color_bgr = (255, 0, 0)
                    else:
                        color_name = "PURPLE"
                        color_bgr = (255, 0, 255)
                    
                    # Show color detected
                    success_frame = frame.copy()
                    cv2.rectangle(success_frame, (150, 200), (490, 280), color_bgr, -1)
                    cv2.rectangle(success_frame, (150, 200), (490, 280), (255, 255, 255), 3)
                    cv2.putText(success_frame, f"COLOR DETECTED: {color_name}", (160, 245),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                    cv2.imshow("Invisible Cloak", success_frame)
                    cv2.waitKey(1000)
                    
                    print(f"   ✅ Color captured: {color_name} (Hue: {cloak_hue})")
            click_pos = None
        
        cv2.imshow("Invisible Cloak", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return
    
    # ============ STEP 3: INVISIBLE CLOAK EFFECT ============
    print("\n✨ STEP 3: INVISIBLE CLOAK ACTIVE!")
    print("   Wear the cloth and watch it disappear!")
    print("   Controls: +/- adjust tolerance, m=mask, q=quit")
    
    show_mask = False
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        
        # Create mask for cloak color
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Handle red color wrap-around (using lower saturation/value thresholds for better detection)
        sat_min = 30  # Lower saturation threshold for broader detection
        val_min = 30  # Lower value threshold to catch darker shades
        
        if cloak_hue < 10:
            lower1 = np.array([0, sat_min, val_min], dtype=np.uint8)
            upper1 = np.array([cloak_hue + hue_tolerance, 255, 255], dtype=np.uint8)
            lower2 = np.array([180 - hue_tolerance, sat_min, val_min], dtype=np.uint8)
            upper2 = np.array([180, 255, 255], dtype=np.uint8)
            mask = cv2.inRange(hsv, lower1, upper1) | cv2.inRange(hsv, lower2, upper2)
        elif cloak_hue > 170:
            lower1 = np.array([cloak_hue - hue_tolerance, sat_min, val_min], dtype=np.uint8)
            upper1 = np.array([180, 255, 255], dtype=np.uint8)
            lower2 = np.array([0, sat_min, val_min], dtype=np.uint8)
            upper2 = np.array([hue_tolerance, 255, 255], dtype=np.uint8)
            mask = cv2.inRange(hsv, lower1, upper1) | cv2.inRange(hsv, lower2, upper2)
        else:
            lower = np.array([max(0, cloak_hue - hue_tolerance), sat_min, val_min], dtype=np.uint8)
            upper = np.array([min(180, cloak_hue + hue_tolerance), 255, 255], dtype=np.uint8)
            mask = cv2.inRange(hsv, lower, upper)
        
        # Clean up mask with stronger operations
        kernel_small = np.ones((3, 3), np.uint8)
        kernel_large = np.ones((7, 7), np.uint8)
        
        # Remove noise
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_small, iterations=2)
        # Fill holes
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_large, iterations=3)
        # Expand the mask to cover edges
        mask = cv2.dilate(mask, kernel_large, iterations=3)
        
        # === ALPHA BLENDING IMPLEMENTATION ===
        # Blur the mask to create soft edges (alpha channel)
        mask_blur = cv2.GaussianBlur(mask, (21, 21), 0)
        alpha = mask_blur.astype(float) / 255.0
        
        # Invert alpha for foreground
        alpha_inv = 1.0 - alpha
        
        # Convert frames to float for blending
        frame_f = frame.astype(float)
        background_f = background.astype(float)
        
        # Blend: Background * Alpha + Foreground * (1 - Alpha)
        # Use cv2.multiply for broadcasting alpha steps
        for c in range(3):
            background_f[:, :, c] = background_f[:, :, c] * alpha
            frame_f[:, :, c] = frame_f[:, :, c] * alpha_inv
            
        result = cv2.add(background_f, frame_f).astype(np.uint8)
        
        # Draw UI
        cv2.rectangle(result, (0, 0), (640, 35), (30, 30, 30), -1)
        cv2.putText(result, f"INVISIBLE CLOAK ACTIVE | Tolerance: {hue_tolerance}", (10, 25),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv2.putText(result, "+/- : Tolerance | m : Mask | q : Quit", (350, 25),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (180, 180, 180), 1)
        
        # Show mask if enabled
        if show_mask:
            mask_small = cv2.resize(mask, (160, 120))
            mask_color = cv2.cvtColor(mask_small, cv2.COLOR_GRAY2BGR)
            result[350:470, 470:630] = mask_color
            cv2.putText(result, "MASK", (475, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1)
        
        cv2.imshow("Invisible Cloak", result)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('m'):
            show_mask = not show_mask
        elif key == ord('+') or key == ord('='):
            hue_tolerance = min(40, hue_tolerance + 2)
            print(f"   Tolerance: {hue_tolerance}")
        elif key == ord('-'):
            hue_tolerance = max(5, hue_tolerance - 2)
            print(f"   Tolerance: {hue_tolerance}")
        elif key == ord('s'):
            cv2.imwrite(f"invisible_{int(time.time())}.jpg", result)
            print("   📸 Screenshot saved!")
    
    cap.release()
    cv2.destroyAllWindows()
    print("\n✅ Done!")

if __name__ == "__main__":
    main()
