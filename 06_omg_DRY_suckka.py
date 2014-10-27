# I wont go over the things covered in the last section. If something here is
# not covered by a comment look back a step.

from random import randint

import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((700, 800))

image = pygame.image.load('assets/sprite_sheet.png')

game_running = True


ship_x = screen.get_width() / 2
ship_y = screen.get_height()-40

sprite_width, sprite_height = (34, 34)
ship_sprite_area = (0*sprite_width, 2*sprite_height,
                    sprite_width, sprite_height)

bullet_sprite_area = (0*sprite_width, 6*sprite_height,
                      sprite_width, sprite_height)

star_sprite_areas = []
for n in [0,1]:
    for r in [0,1]:
        star_sprite_areas.append(
            ((3+n)*sprite_width, (3+r)*sprite_height, sprite_width, sprite_height))

class Bullet(object):
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.last_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.last_time
        self.y -= 1 * delta_time
        self.last_time = current_time

class Star(object):
    def __init__(self, start_x, speed=1):
        self.x = start_x
        self.y = 0
        self.speed = speed
        self.last_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.last_time
        self.y += ((self.speed) * delta_time) * 0.035
        self.last_time = current_time

bullets = []
stars = []

while game_running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_running = False
            if event.key == K_LEFT:
                ship_x -= 5
            if event.key == K_RIGHT:
                ship_x += 5
            if event.key == K_SPACE:
                bullets.append(Bullet(ship_x+2, ship_y))
            if event.key == K_s:
                pass
    if randint(1,15) == 10:
        rand_x_pos = randint(0, screen.get_width())
        stars.append(
            Star(rand_x_pos, randint(10,20))
        )

    screen.fill((0, 0, 0))

    dead_bullets = []
    dead_stars = []

    for bullet in bullets:
        bullet.update()
        if bullet.y <= 0:
            dead_bullets.append(bullet)
        screen.blit(image, (bullet.x, bullet.y, 0, 0), bullet_sprite_area)

    for star in stars:
        star.update()
        if star.y >= screen.get_height():
            dead_stars.append(star)
        screen.blit(image, (star.x, star.y, 0, 0), star_sprite_areas[0])

    for dead in dead_bullets:
            bullets.remove(dead)
    for dead in dead_stars:
            stars.remove(dead)

    screen.blit(image, (ship_x, ship_y, 0, 0), ship_sprite_area)

    pygame.display.flip()

print 'Fin.'
