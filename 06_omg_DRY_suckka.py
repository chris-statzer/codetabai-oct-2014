# I wont go over the things covered in the last section. If something here is
# not covered by a comment look back a step.

from random import randint

import pygame
from pygame.locals import *

from spritesheet import SpriteSheet

pygame.init()
screen = pygame.display.set_mode((700, 800))

sprite_sheet = SpriteSheet('assets/shooter_sheet.sheet')




class Bullet(object):
    def __init__(self, start_x, start_y):
        self.sprite = sprite_sheet.new_sprite('bullet')
        self.sprite.rect.x = start_x
        self.sprite.rect.y = start_y
        self.last_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.last_time
        self.sprite.rect.y -= 1 * delta_time
        self.last_time = current_time

class Star(object):
    def __init__(self, start_x, speed=1):
        self.sprite = sprite_sheet.new_sprite('star_y_{}'.format(randint(1,3)))
        self.sprite.rect.x = start_x
        self.sprite.rect.y = 0
        self.y = 0
        self.speed = speed
        self.last_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.last_time
        self.y += ((self.speed) * delta_time) * 0.035
        self.sprite.rect.y = self.y
        self.last_time = current_time

class Ship(object):
    def __init__(self, start_x, start_y):
        self.sprite = sprite_sheet.new_sprite('ship')
        self.sprite.rect.x = start_x
        self.sprite.rect.y = start_y
        self.last_time = pygame.time.get_ticks()
        self.h_velocity = 0
        self.x = start_x

    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.last_time
        self.x += ((self.h_velocity) * delta_time) * 0.335
        self.sprite.rect.x = self.x
        self.last_time = current_time


ship = Ship(screen.get_width() / 2, screen.get_height()-40)

bullets = []
stars = []

background_group = pygame.sprite.RenderUpdates()
friendly_group = pygame.sprite.RenderUpdates()

friendly_group.add(ship.sprite)

game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_running = False
            if event.key == K_LEFT:
                ship.h_velocity += -1
            if event.key == K_RIGHT:
                ship.h_velocity += 1
            if event.key == K_SPACE:
                new_bullet = Bullet(ship.sprite.rect.x, ship.sprite.rect.y-20)
                bullets.append(new_bullet)
                friendly_group.add(new_bullet.sprite)
        if event.type == KEYUP:
            if event.key == K_LEFT:
                ship.h_velocity -= -1
            if event.key == K_RIGHT:
                ship.h_velocity -= 1

    if randint(1,150) == 1:
        rand_x_pos = randint(0, screen.get_width())
        new_star = Star(rand_x_pos, randint(15,20))
        stars.append(new_star)
        background_group.add(new_star.sprite)

    screen.fill((0, 0, 0))

    dead_bullets = []
    for bullet in bullets:
        bullet.update()
        if bullet.sprite.rect.y <= 0:
            dead_bullets.append(bullet)
    for dead in dead_bullets:
            bullets.remove(dead)
            dead.sprite.kill()

    dead_stars = []
    for star in stars:
        star.update()
        if star.sprite.rect.y >= screen.get_height():
            dead_stars.append(star)
    for dead in dead_stars:
            stars.remove(dead)
            dead.sprite.kill()

    ship.update()

    update_rects = []
    update_rects += background_group.draw(screen)
    update_rects += friendly_group.draw(screen)
    pygame.display.update(update_rects)

print 'Fin.', stars, bullets
