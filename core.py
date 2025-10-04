# main.py
# This is the main script to run the Rubik's Cube solver application.

import cv2
import numpy as np
import colorama
import time

# Import from our custom modules
from config import stickers, state, check_state, color
from vision_utils import (color_detect, draw_stickers, fill_stickers,
                          draw_preview_stickers, texton_preview_stickers)
from cube_logic import solve
from solver_visualizer import process

def main():
    """Main function to run the application."""
    # --- Initialization ---
    colorama.init()
    RED = colorama.Fore.RED
    GREEN = colorama.Fore.GREEN
    MAGENTA = colorama.Fore.MAGENTA
    RESET = colorama.Fore.RESET

    # (Welcome banner print statements can be placed here)
    print(f"{MAGENTA}Please refer to the preview window for scanning instructions.{RESET}")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print(f"{RED}Error: Could not open video stream.{RESET}")
        return

    preview = np.zeros((700, 800, 3), np.uint8)
    
    # --- Main Application Loop ---
    while True:
        ret, img = cap.read()
        if not ret:
            print("Failed to grab frame. Exiting.")
            break
        
        hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # --- Update UI and State ---
        preview[:] = (0, 0, 0)
        draw_stickers(img, stickers, 'main')
        draw_stickers(img, stickers, 'current')
        fill_stickers(preview, stickers, state)
        draw_preview_stickers(preview, stickers)
        texton_preview_stickers(preview)

        # Detect colors from the 9 main sticker regions
        current_scan = []
        for i in range(9):
            hsv_val = hsv_frame[stickers['main'][i][1] + 15][stickers['main'][i][0] + 15]
            color_name = color_detect(hsv_val[0], hsv_val[1], hsv_val[2])
            current_scan.append(color_name)
            
            x, y = stickers['current'][i]
            cv2.rectangle(img, (x, y), (x + 30, y + 30), color[color_name], -1)

        # --- Handle User Input ---
        k = cv2.waitKey(1) & 0xFF
        if k == 27: break # ESC
        elif k == ord('u'): state['up'] = current_scan; check_state.append('u')
        elif k == ord('r'): state['right'] = current_scan; check_state.append('r')
        elif k == ord('l'): state['left'] = current_scan; check_state.append('l')
        elif k == ord('d'): state['down'] = current_scan; check_state.append('d')
        elif k == ord('f'): state['front'] = current_scan; check_state.append('f')
        elif k == ord('b'): state['back'] = current_scan; check_state.append('b')
        elif k == ord('\r'): # Enter key
            if len(set(check_state)) == 6:
                try:
                    solution_moves = solve()
                    op_list = solution_moves.split(' ')
                    process(op_list)
                except Exception as e:
                    print(f"{RED}Error during solving: {e}{RESET}")
            else:
                print(f"{RED}All 6 sides have not been scanned.{RESET}")

        cv2.imshow('preview', preview)
        cv2.imshow('frame', img[0:500, 0:500])

    # --- Cleanup ---
    cap.release()
    cv2.destroyAllWindows()
    colorama.deinit()

if __name__ == '__main__':
    main()