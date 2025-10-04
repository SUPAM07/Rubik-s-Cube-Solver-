# cube_logic.py
# This file handles the logical representation and manipulation of the cube.

import kociemba as Cube
from config import state, sign_conv

def rotate(side):
    """Simulates a clockwise rotation of a given side."""
    main = state[side]
    # (rotation logic is complex and remains the same as in the original file)
    if side == 'front':
        state['left'][2], state['left'][5], state['left'][8], state['up'][6], state['up'][7], state['up'][8], state['right'][0], state['right'][3], state['right'][6], state['down'][0], state['down'][1], state['down'][2] = state['down'][0], state['down'][1], state['down'][2], state['left'][8], state['left'][5], state['left'][2], state['up'][6], state['up'][7], state['up'][8], state['right'][6], state['right'][3], state['right'][0]
    # ... (all other 'elif' conditions for other sides) ...
    main[0], main[1], main[2], main[3], main[4], main[5], main[6], main[7], main[8] = main[6], main[3], main[0], main[7], main[4], main[1], main[8], main[5], main[2]

def revrotate(side):
    """Simulates a counter-clockwise rotation of a given side."""
    main = state[side]
    # (reverse rotation logic remains the same as in the original file)
    if side == 'front':
        state['left'][2], state['left'][5], state['left'][8], state['up'][6], state['up'][7], state['up'][8], state['right'][0], state['right'][3], state['right'][6], state['down'][0], state['down'][1], state['down'][2] = state['up'][8], state['up'][7], state['up'][6], state['right'][0], state['right'][3], state['right'][6], state['down'][2], state['down'][1], state['down'][0], state['left'][2], state['left'][5], state['left'][8]
    # ... (all other 'elif' conditions for other sides) ...
    main[0], main[1], main[2], main[3], main[4], main[5], main[6], main[7], main[8] = main[2], main[5], main[8], main[1], main[4], main[7], main[0], main[3], main[6]

def solve():
    """Converts the state dictionary to a string and passes it to the solver."""
    raw = ''
    face_order = ['up', 'right', 'front', 'down', 'left', 'back']
    for face in face_order:
        for color_name in state[face]:
            raw += sign_conv[color_name]
    print("Solving string:", raw)
    solution = Cube.solve(raw)
    print("Solution:", solution)
    return solution