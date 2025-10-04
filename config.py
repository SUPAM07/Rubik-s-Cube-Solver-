# config.py
# This file contains all the configuration variables and data structures.

import cv2

# --- Cube State and Mappings ---

# Represents the color of each sticker on each face
state = {
    'up':    ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'],
    'right': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'],
    'front': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'],
    'down':  ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'],
    'left':  ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'],
    'back':  ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']
}

# Maps color names to the character representation required by the kociemba solver
sign_conv = {
    'green': 'F', 'white': 'U', 'blue': 'B',
    'red': 'R', 'orange': 'L', 'yellow': 'D'
}

# --- UI and Display Constants ---

# Defines the BGR color values for UI drawing
color = {
    'red':    (0, 0, 255),     'orange': (0, 165, 255), 'blue': (255, 0, 0),
    'green':  (0, 255, 0),     'white':  (255, 255, 255), 'yellow': (0, 255, 255)
}

# Defines pixel coordinates for drawing sticker rectangles
stickers = {
    'main': [[200, 120], [300, 120], [400, 120], [200, 220], [300, 220], [400, 220], [200, 320], [300, 320], [400, 320]],
    'current': [[20, 20], [54, 20], [88, 20], [20, 54], [54, 54], [88, 54], [20, 88], [54, 88], [88, 88]],
    'preview': [[20, 130], [54, 130], [88, 130], [20, 164], [54, 164], [88, 164], [20, 198], [54, 198], [88, 198]],
    'left': [[50, 280], [94, 280], [138, 280], [50, 324], [94, 324], [138, 324], [50, 368], [94, 368], [138, 368]],
    'front': [[188, 280], [232, 280], [276, 280], [188, 324], [232, 324], [276, 324], [188, 368], [232, 368], [276, 368]],
    'right': [[326, 280], [370, 280], [414, 280], [326, 324], [370, 324], [414, 324], [326, 368], [370, 368], [414, 368]],
    'up': [[188, 128], [232, 128], [276, 128], [188, 172], [232, 172], [276, 172], [188, 216], [232, 216], [276, 216]],
    'down': [[188, 434], [232, 434], [276, 434], [188, 478], [232, 478], [276, 478], [188, 522], [232, 522], [276, 522]],
    'back': [[464, 280], [508, 280], [552, 280], [464, 324], [508, 324], [552, 324], [464, 368], [508, 368], [552, 368]],
}

# Defines coordinates and properties for text labels on the preview UI
font = cv2.FONT_HERSHEY_SIMPLEX
textPoints = {
    'up':    [['U', 242, 202], ['W', (255, 255, 255), 260, 208]], 'right': [['R', 380, 354], ['R', (0, 0, 255), 398, 360]],
    'front': [['F', 242, 354], ['G', (0, 255, 0), 260, 360]],   'down':  [['D', 242, 508], ['Y', (0, 255, 255), 260, 514]],
    'left':  [['L', 104, 354], ['O', (0, 165, 255), 122, 360]],  'back':  [['B', 518, 354], ['B', (255, 0, 0), 536, 360]],
}

# --- Application State Variables ---
check_state = [] # Tracks which sides have been scanned