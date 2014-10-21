# I wont go over the things covered in the last section. If something here is not
# covered by a comment look back a step.

import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((800, 600))

# Here we are gonna use the pygame.image module to load a PNG sprite sheet.
# It is important to note that using the SDL C library is not this simple.
# Pygame has a ton of extras and supports lots of formats using various
# 3rd party libs.
image = pygame.image.load('assets/sprite_sheet.png')

game_running = True

# Here we are going to perform what is called a 'blit'. You can understand it a
# little better if you want by looking at http://en.wikipedia.org/wiki/Bit_blit
# You really don't need to know how it works honestly it is basically just
# a 'draw' operation that allows you to draw one surface onto another.
# here our target is the screen surface we got earlier from the set_mode method.
# This surface is special in that anything you do to it happens DIRECTLY to the
# screen. for now this is fine, but later we are gonna want to make better use
# of our video cards memory. The first argument is the image we loaded above.
# the second argument is the area where we want the image to be drawn. It is
# a python tuple with the values (x, y, width, height). For now the height
# doesnt matter to us so we just leave it at 0.
screen.blit(image, (10, 20, 0, 0))

while game_running:
    for event in pygame.event.get():
        print event
        if event.type == KEYDOWN:
            game_running = False

print 'Fin.'