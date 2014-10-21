# I wont go over the things covered in the last section. If something here is not
# covered by a comment look back a step.

import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((800, 600))

image = pygame.image.load('assets/sprite_sheet.png')

game_running = True


# Our ship is only going be be able to move left and right so we just need
# an X axis to control it. lets set its initial value to the middle of the
# screen by getting the width of the screen using get_width and dividing by 2.
ship_x = screen.get_width() / 2

# Also set a y value for the ship. this wont change but we will calculate it
# to be 40 pixels above the bottom of the screen.
ship_y = screen.get_height()-40

# Next we need an offset on our sprite sheet. Our sprites are 18x18 and the ship
# is on the 3rd row and the first column.
# First lets define some constants for our sprites so we can do some math later
sprite_width, sprite_height = (36, 36)

# Here we are going to calculate a sub rectangle. We know our sprite is on the
# first column so that's 0 times the sprites width. We know our sprite is on
# the 3rd row so that's 2 times the sprite height (don't forget almost all number
# ranges in compsci start at 0!!!)
# This gives us a sub rectangle of (0, 72, 36, 36). what this means is when we
# do our blit pygame is only going to use a potion of our sprite we loaded. Its
# going to draw a 36x36 chunk of the sprite sheet starting at x:0 y:72
ship_sprite_area = (0*sprite_width, 2*sprite_height, sprite_width, sprite_height)

while game_running:
    for event in pygame.event.get():
        print event
        if event.type == KEYDOWN:
            # Here we make some changes to how we are handling keys.
            # Now instead of just ending the program when a key is pressed we
            # are going to check some individual keys and do some actions based
            # on which is pressed.
            # First we are gonna test for the escape key. if its the key that
            # was pressed then we are gonna kill the program.
            if event.key == K_ESCAPE:
                game_running = False
            # Next we are gonna test the left and right arrow keys. If these
            # are pressed we will add or subtract 5 pixels from the ships x
            # position and now it will move on the screen!
            if event.key == K_LEFT:
                ship_x -= 5
            if event.key == K_RIGHT:
                ship_x += 5

    # After we process our events we want to do our drawing
    # The first thing we need to do is fill the screen with an all black.
    # The fill method takes a 3 item tuple of color values 0-255.
    # (red, green, blue)
    screen.fill((0, 0, 0))

    # Next we will blit our ship using the variables we calculated earlier.
    # the 3rd argument is the area we calculated. That tells pygame to only
    # blit only the portion of the sheet that contains our ship.
    screen.blit(image, (ship_x, ship_y, 0, 0), ship_sprite_area)

    # Last in order to get our screen to update beyond the first draw we need to
    # 'flip' the display. This tells pygame that we are done with our drawing
    # and the operating system can repaint the window.
    pygame.display.flip()


print 'Fin.'