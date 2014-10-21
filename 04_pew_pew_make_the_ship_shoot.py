# I wont go over the things covered in the last section. If something here is not
# covered by a comment look back a step.

import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((800, 600))

image = pygame.image.load('assets/sprite_sheet.png')

game_running = True


ship_x = screen.get_width() / 2
ship_y = screen.get_height()-40

sprite_width, sprite_height = (36, 36)
ship_sprite_area = (0*sprite_width, 2*sprite_height, sprite_width, sprite_height)

# Just like before we are gonna calculate a sub rectangle for the bullet sprite.
# it is on the 3rd row and the 3rd column. (remember ranges start at 0!!!)
bullet_sprite_area = (2*sprite_width, 2*sprite_height, sprite_width-4, sprite_height)


# Here is our first exposure to the python class
class Bullet(object):
    """ Our bullet has a state that need to be kept and in addition we will
    place the update code here as well. A bullet knows what its suppose to do
    and this design will help us keep code duplication to a minimum.
    """
    def __init__(self, start_x, start_y):
        """The __init__ method is a special method of python classes that is
        analogous to constructors in other languages. Here we can accept
        data from the creation call and build an initial state for the bullet"""
        # Here we set the initial position of the bullet
        self.x = start_x
        self.y = start_y
        # Using the method get_ticks we can store the time in milliseconds
        # that the bullet is created. We will need this later in update() to
        # calculate the movement of the bullet on the screen.
        self.last_time = pygame.time.get_ticks()

    def update(self):
        """Our update method is going to get called with every loop of our
        game. Here we are gonna update the location of the bullet using
        the time functions provided by pygame"""
        # We need a temp local variable with the current time in milliseconds
        current_time = pygame.time.get_ticks()
        # We can calculate the delta by subtracting the last time from our
        # current time and that gives us the total milliseconds since the
        # last update
        delta_time = current_time - self.last_time
        # The bullets move up on the screen so we will subtract the delta * 1px
        # from the y axis of the bullet. This is VERY crude and only for an
        # example. This does not take into account actual time as a faster
        # computer will do this faster. The math to make this framerate
        # independent is not complicated but requires more variables.
        self.y -= 1 * delta_time
        # When we are done moving the bullet we will reset out last_time member
        # to the current time so the value is fresh and we can get a proper
        # value for the amount of time that has passed since last call.
        self.last_time = current_time

# We will store our active bullets in a simple array.
bullets = []

while game_running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_running = False
            if event.key == K_LEFT:
                ship_x -= 5
            if event.key == K_RIGHT:
                ship_x += 5
            # A small addition to our key handling code. when the spacebar is
            # pressed we can add a new bullet to the play area. here I use the
            # current location of our ship.
            if event.key == K_SPACE:
                bullets.append(Bullet(ship_x+2, ship_y))
                print 'shoot'

    screen.fill((0, 0, 0))

    # We need a place to store bullets that need to be removed from our array
    # our bullet class has a member alive which will be set if the y position
    # goes off the screen or later when they can hit enemies. The reason we
    # have to track these separate is, you can not modify a sequence while
    # you are looping through it with the for keyword.
    dead_bullets = []

    # Lets iterate all the bullets, update them and check if they need to be
    # deleted, then draw them.
    for bullet in bullets:
        bullet.update()
        # Here we check if the y position of the bullet is off the screen
        if bullet.y <= 0:
            # if so append it to dead_bullets
            dead_bullets.append(bullet)
        # Here we draw each bullet at its new position
        screen.blit(image, (bullet.x, bullet.y, 0, 0), bullet_sprite_area)

    # now that we have a list of bullets that are no longer visible to the
    # player and cant effect the game. we can iterate over it and delete them
    # from our collection of active bullets
    for dead in dead_bullets:
            print 'removing', dead
            bullets.remove(dead)

    screen.blit(image, (ship_x, ship_y, 0, 0), ship_sprite_area)

    pygame.display.flip()


print 'Fin.'