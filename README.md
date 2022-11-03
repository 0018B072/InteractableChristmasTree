# InteractableChristmasTree

This openCV program will recognize the qr code, grab its value/id, and use the center of the poly to find the distance from a fixed point on the screen.
After grabbing the qr code id, it will tell the arduino using a LORA radio module what specific LED to change colors. Depending on how big the distance
the center of the poly is to the fixed point, it will change colors from red to blue in a gradient.
