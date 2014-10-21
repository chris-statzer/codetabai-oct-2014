
# First we need to import the pygame module so we can access all of the
# graphics/input/timing routines.
import pygame

# While in most cases importing * from any module is a faux pas.... in the
# case of pygame the locals memember of the module was designed to be
# imported so you have access to the constants exposed by SDL
from pygame.locals import *


# Before we can do anything we need to call the init method the module provides
# this sets up some constants and OS specific stuff SDL needs to deal with
pygame.init()


# Next we will setup the screen resolution we want and get a reference
# to a pygame.Surface object. We will cover the pygame.Surface later.
screen = pygame.display.set_mode((800, 600))


# Here we are going to set a variable to hold the state of the applications
# execution. Using the while keyword below we keep the application running
# in a loop until we set the value of game_running to False
game_running = True
while game_running:
    # Part of the 'loop' of our game is processing input from the keyboard
    # or mouse (or any other input device you can think of as SDL even has
    # support for things like WiiMote)
    # pygame.event.get returns to us a list of every event that has happened
    # since the last time the loop was run. We will use a for loop to process
    # each one. We will also print the events to the console so you can see
    # what is happening. For now if there are ANY keydown events then we
    # set game_running to False and end the loop.
    for event in pygame.event.get():
        print event
        if event.type == KEYDOWN:
            game_running = False


print 'Fin.'