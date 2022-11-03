# InteractableChristmasTree

1 different QR Code will be surrounding each LED ball with 3 cameras covering 3 axis' of the Christmas tree.
The openCV program will have a point in 3d space in which the cameras will detect how far the center of the QR code is from the original point using distance formula.

This openCV program will recognize the qr code, grab its value/id, and use the center of the poly to find the distance from a fixed point on the screen.
After grabbing the qr code id, it will tell the arduino using a LORA radio module what specific LED to change colors. Depending on how big the distance
the center of the poly is to the fixed point, it will change colors from red to blue in a gradient.
