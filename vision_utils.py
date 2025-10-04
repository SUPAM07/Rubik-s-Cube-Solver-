# vision_utils.py
# This file contains all computer vision and UI drawing helper functions.

import cv2
from config import color, textPoints, font

def color_detect(h, s, v):
    """Identifies a color name based on its HSV values."""
    if s < 38: return 'white'
    if (h >= 0 and h <= 1) or (h >= 170 and h <= 179): return 'red'
    if h >= 2 and h <= 15: return 'orange'
    if h >= 18 and h <= 38: return 'yellow'
    if h >= 40 and h <= 85: return 'green'
    if h >= 90 and h <= 130: return 'blue'
    return 'white'

def draw_stickers(frame, sticker_set, name):
    """Draws outlines for a specific set of stickers on a frame."""
    for x, y in sticker_set[name]:
        cv2.rectangle(frame, (x, y), (x + 30, y + 30), (255, 255, 255), 2)

def draw_preview_stickers(frame, sticker_set):
    """Draws the outlines for all 6 faces on the preview window."""
    for name in ['front', 'back', 'left', 'right', 'up', 'down']:
        for x, y in sticker_set[name]:
            cv2.rectangle(frame, (x, y), (x + 40, y + 40), (255, 255, 255), 2)

def texton_preview_stickers(frame):
    """Draws face labels (e.g., 'U' for Up) on the preview window."""
    for name in textPoints:
        sym, x1, y1 = textPoints[name][0]
        cv2.putText(frame, sym, (x1, y1), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
        sym, col, x1, y1 = textPoints[name][1]
        cv2.putText(frame, sym, (x1, y1), font, 0.5, col, 1, cv2.LINE_AA)

def fill_stickers(frame, sticker_set, sides):
    """Fills the sticker outlines on the preview window with their current colors."""
    for side, colors in sides.items():
        for i, (x, y) in enumerate(sticker_set[side]):
            cv2.rectangle(frame, (x, y), (x + 40, y + 40), color[colors[i]], -1)