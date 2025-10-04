# Automated Rubik's Cube Solver

Situation:
 The manual process of solving a Rubik's Cube is complex and relies on memorizing algorithms. I aimed to create a desktop application to automate this process using computer vision.

Task:
 My goal was to develop a Python application that could analyze a physical Rubik's Cube through a webcam, calculate the most efficient solution, and present the steps to the user in a clear, visual format.

Action:
Engineered a real-time video processing pipeline using OpenCV to capture the cube's state, implementing robust color detection by converting the feed to the HSV color space to handle varying light conditions.

Designed and built an interactive GUI with OpenCV's drawing functions to guide the user through the scanning process for all six faces of the cube.

Integrated the Kociemba two-phase algorithm to efficiently compute the optimal solution from the captured cube state, translating the state into a solver-compatible string format.

Developed a separate visualization module to display each move of the solution step-by-step, enhancing the user experience.

Refactored the initial prototype from a single script into a modular, multi-file architecture to improve code readability, maintainability, and scalability.

Result:
Successfully delivered a fully functional application that accurately recognizes a cube's configuration and provides an optimal, easy-to-follow solution.

Demonstrated proficiency in Python, OpenCV, NumPy, computer vision fundamentals, UI design, and modular software architecture.