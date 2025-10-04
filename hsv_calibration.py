import cv2
import numpy as np

# --- Configuration ---
# Using the same coordinates as your main solver script
stickers = {
    'main': [
        [200, 120], [300, 120], [400, 120],
        [200, 220], [300, 220], [400, 220],
        [200, 320], [300, 320], [400, 320]
    ],
    'preview': [ # A small 3x3 grid to show detected colors
        [20, 20], [54, 20], [88, 20],
        [20, 54], [54, 54], [88, 54],
        [20, 88], [54, 88], [88, 88]
    ]
}

# BGR color values for drawing the preview
color_bgr = {
    'red':(0,0,255), 'orange':(0,165,255), 'blue':(255,0,0),
    'green':(0,255,0), 'white':(255,255,255), 'yellow':(0,255,255)
}

# --- Color Detection Logic (for on-screen preview) ---
def color_detect(h, s, v):
    """A basic detection function to provide visual feedback."""
    if s < 38: return 'white'
    if (h >= 0 and h <= 10) or (h >= 170 and h <= 179): return 'red'
    elif h > 10 and h <= 25: return 'orange'
    elif h > 25 and h <= 35: return 'yellow'
    elif h > 35 and h <= 85: return 'green'
    elif h > 85 and h <= 130: return 'blue'
    return 'white'

# --- Main Program ---
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

window_name = 'HSV Grid Calibrator'
cv2.namedWindow(window_name)

print("Align a face of the cube with the 9-box grid.")
print("The terminal will show the HSV values for all 9 stickers.")
print("Press 'Esc' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # --- Clear the terminal for clean output ---
    # On Windows, use 'cls'. On macOS/Linux, use 'clear'.
    # For simplicity, we just print separator lines.
    print("\033[H\033[J", end="") # Clears the console screen
    print("--- Reading HSV Values (Press Esc to Quit) ---")

    # --- Process each of the 9 sticker locations ---
    for i, (x, y) in enumerate(stickers['main']):
        # Draw the main detection grid on the frame
        cv2.rectangle(frame, (x, y), (x + 80, y + 80), (255, 255, 255), 2)
        
        # Sample a small region of interest (ROI) from the center of the box
        roi = hsv_frame[y + 35:y + 45, x + 35:x + 45]
        
        # Calculate the average HSV value of the ROI
        h, s, v = np.mean(roi, axis=(0, 1)).astype(int)
        
        # Print the HSV value to the terminal
        print(f"Box {i+1}: H={h:3d}, S={s:3d}, V={v:3d}")

        # --- Draw a live preview of detected colors ---
        detected_color_name = color_detect(h, s, v)
        preview_x, preview_y = stickers['preview'][i]
        cv2.rectangle(frame, (preview_x, preview_y), (preview_x + 30, preview_y + 30), color_bgr[detected_color_name], -1)

    # Add a border to the preview area
    cv2.rectangle(frame, (15, 15), (123, 123), (255,255,255), 1)

    # Display the final frame
    cv2.imshow(window_name, frame)

    if cv2.waitKey(500) & 0xFF == 27: # Update every 500ms
        break

# Clean up
cap.release()
cv2.destroyAllWindows()