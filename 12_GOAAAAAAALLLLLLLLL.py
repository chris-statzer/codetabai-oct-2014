

from random import randint

import pygame
from pygame.locals import *

from spritesheet import SpriteSheet


pygame.init()
screen = pygame.display.set_mode((500, 600))

sprite_sheet = SpriteSheet('assets/shooter_sheet.sheet')
star_surface = sprite_sheet.new_surface('star_y_1')
ship_surface = sprite_sheet.new_surface('ship')
bullet_surface = sprite_sheet.new_surface('bullet')
enemy_surface = sprite_sheet.new_surface('enemy_1')

class Star(pygame.sprite.Sprite):
    def __init__(self, surface, speed, start_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.rect = self.image.get_rect()
        self.last_time = pygame.time.get_ticks()
        self.y = 0
        self.rect.x = start_x
        self.speed = speed
        
    def update(self):
        if self.rect.y >= 600:
            self.kill()
            return
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.last_time
        self.y += ((self.speed) * delta_time) * 0.001
        self.rect.y = self.y
        self.last_time = current_time

class Ship(pygame.sprite.Sprite):
    def __init__(self, surface, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.last_time = pygame.time.get_ticks()
        self.h_velocity = 0
        self.x = start_x

    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.last_time
        self.x += ((self.h_velocity) * delta_time) * 0.335
        self.rect.x = self.x
        self.last_time = current_time

class Bullet(pygame.sprite.Sprite):
    def __init__(self, surface, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.last_time = pygame.time.get_ticks()

    def update(self):
        if self.rect.y <= 0:
            self.kill()
            return
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.last_time
        self.rect.y -= 1 * delta_time
        self.last_time = current_time

class Enemy(pygame.sprite.Sprite):
    def __init__(self, surface, speed, start_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.rect = self.image.get_rect()
        self.last_time = pygame.time.get_ticks()
        self.y = 0
        self.rect.x = start_x
        self.speed = speed
        
    def update(self):
        if self.rect.y >= 600:
            self.kill()
            return
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.last_time
        self.y += ((self.speed) * delta_time) * 0.001
        self.rect.y = self.y
        self.last_time = current_time
        
background_group = pygame.sprite.RenderUpdates()
ship_group = pygame.sprite.RenderUpdates()
friendly_bullet_group = pygame.sprite.RenderUpdates()
enemy_group = pygame.sprite.RenderUpdates()

ship = Ship(ship_surface, screen.get_width()/2, screen.get_height()-40)
ship_group.add(ship)

score = 0
score_font = pygame.font.Font(pygame.font.get_default_font(), 16)
font_rect = (0,0,100,30)

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
                new_bullet = Bullet(bullet_surface, ship.rect.x+12, ship.rect.y-20)
                friendly_bullet_group.add(new_bullet)
        if event.type == KEYUP:
            if event.key == K_LEFT:
                ship.h_velocity -= -1
            if event.key == K_RIGHT:
                ship.h_velocity -= 1
    
    if randint(0,100) == 1:
        star_speed = randint(300,400)
        star_x_location = randint(0,screen.get_width())
        new_star = Star(star_surface, star_speed, star_x_location)
        background_group.add(new_star)

    if randint(0,1000) == 1:
        enemy_speed = randint(300,400)
        enemy_x_location = randint(0,screen.get_width())
        new_enemy = Enemy(enemy_surface, enemy_speed, enemy_x_location)
        enemy_group.add(new_enemy)
                
    screen.fill((0,0,0))
    background_group.update()
    ship_group.update()
    friendly_bullet_group.update()
    enemy_group.update()
    
    bullet_hit_list = []
    for bullet in friendly_bullet_group:
        bullet_hit = pygame.sprite.spritecollide(bullet, enemy_group, True)
        if bullet_hit != []:
            bullet_hit_list += bullet_hit
            bullet.kill()
    score += len(bullet_hit_list) * 1000
    
    

    updated_rects = []    
    updated_rects += background_group.draw(screen)
    updated_rects += ship_group.draw(screen)
    updated_rects += friendly_bullet_group.draw(screen)
    updated_rects += enemy_group.draw(screen)
    
    score_surface = score_font.render('Score: {}'.format(score), True, (255,255,255))
    screen.blit(score_surface, font_rect)
    updated_rects += [score_surface.get_rect()]
    
    pygame.display.update(updated_rects)


