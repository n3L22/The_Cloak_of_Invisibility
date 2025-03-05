import cv2
import numpy as np
import time

def replace_blue_with_background():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    print("Webcam initialized.")
    
    # Wait a moment for the camera to initialize
    time.sleep(2)
    
    # Capture background
    print("Capturing background in 3 seconds. Please move out of frame...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    ret, background = cap.read()
    if not ret:
        print("Error: Failed to capture background")
        cap.release()
        return
    
    print("Background captured successfully!")
    print("Processing video stream. Press 'q' to quit.")
    
    while True:
        # Capture current frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to capture image")
            break
        
        # Convert current frame to HSV (better for color detection)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Define range for blue color in HSV
        # You may need to adjust these values based on lighting and the specific blue shade
        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([130, 255, 255])
        
        # Create a mask for blue color
        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        # Apply some morphological operations to clean up the mask
        kernel = np.ones((5, 5), np.uint8)
        blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
        blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_CLOSE, kernel)
        
        # Create inverse of the mask for the current frame
        frame_mask = cv2.bitwise_not(blue_mask)
        
        # Extract the region of interest from both background and current frame
        background_region = cv2.bitwise_and(background, background, mask=blue_mask)
        frame_region = cv2.bitwise_and(frame, frame, mask=frame_mask)
        
        # Combine the two regions to get the final result
        result = cv2.add(background_region, frame_region)
        
        # Display the original, mask, and result
        cv2.imshow('Original', frame)
        cv2.imshow('Blue Mask', blue_mask)
        cv2.imshow('Result (Blue Replaced with Background)', result)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    replace_blue_with_background()