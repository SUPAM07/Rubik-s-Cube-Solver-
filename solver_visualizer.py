# solver_visualizer.py
# This file handles the step-by-step visualization of the solution.

import cv2
import numpy as np
from config import stickers, state, font
from cube_logic import rotate, revrotate
from vision_utils import fill_stickers, draw_preview_stickers, texton_preview_stickers

def process(operation_list):
    """Processes and displays the solution moves step-by-step."""
    replace = {
        "F": [rotate, 'front'], "F2": [rotate, 'front', 'front'], "F'": [revrotate, 'front'],
        "U": [rotate, 'up'],    "U2": [rotate, 'up', 'up'],       "U'": [revrotate, 'up'],
        "L": [rotate, 'left'],  "L2": [rotate, 'left', 'left'],   "L'": [revrotate, 'left'],
        "R": [rotate, 'right'], "R2": [rotate, 'right', 'right'], "R'": [revrotate, 'right'],
        "D": [rotate, 'down'],  "D2": [rotate, 'down', 'down'],   "D'": [revrotate, 'down'],
        "B": [rotate, 'back'],  "B2": [rotate, 'back', 'back'],   "B'": [revrotate, 'back']
    }
    
    solution_preview = np.zeros((700, 800, 3), np.uint8)
    for move in operation_list:
        # Apply the move(s) to the virtual cube state
        for i in range(len(replace[move]) - 1):
            replace[move][0](replace[move][i + 1])

        # Redraw the preview window with the new state
        solution_preview[:] = (0, 0, 0)
        fill_stickers(solution_preview, stickers, state)
        draw_preview_stickers(solution_preview, stickers)
        texton_preview_stickers(solution_preview)
        cv2.putText(solution_preview, f"Move: {move}", (550, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Solution', solution_preview)
        
        if cv2.waitKey(2000) & 0xFF == 27: # 2-second delay per move
            break