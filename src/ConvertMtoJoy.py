import pygame
import vgamepad as vg
import numpy as np

# Setting up mouse tracking
mouse = pygame.mouse
# Setting up virtual joystick
vjoy = vg.VX360()
# Setting up the screen for interface
screen = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Getting the mouse position
    x, y = mouse.get_pos()

    # Convert the mouse position to joystick axes
    x_axis = ((x - 320) / 320)
    y_axis = ((y - 240) / 240)

    # Set the virtual joystick axes
    vjoy.update_axis(0, x_axis)
    vjoy.update_axis(1, y_axis)

    # Get the mouse buttons
    left, middle, right = mouse.get_pressed()

    # Set the virtual joystick buttons
    vjoy.update_button(0, left)
    vjoy.update_button(1, middle)
    vjoy.update_button(2, right)

    # Update the screen
    pygame.display.flip()
 
