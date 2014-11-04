from random import randint, uniform

import pygame
from pygame.locals import *

from shootersprite import ShooterSprite
from spritesheet import SpriteSheet

sprite_sheet = SpriteSheet('assets/shooter_sheet.sheet')
star_surface = sprite_sheet.new_surface('star_y_1')
ship_surface = sprite_sheet.new_surface('ship')
bullet_surface = sprite_sheet.new_surface('bullet')
enemy_surface = sprite_sheet.new_surface('enemy_1')


class ShipSprite(ShooterSprite):
    def __init__(self, surface, start_x, start_y):
        ShooterSprite.__init__(self, surface, start_x, start_y, 0, 0)


class StarSprite(ShooterSprite):
    def __init__(self, surface, start_x, vel_y):
        ShooterSprite.__init__(self, surface, start_x, 0, 0, vel_y)
        
    def update(self):
        ShooterSprite.update(self)
        if self.y >= 600:
            self.kill()
            

class BulletSprite(ShooterSprite):
    def __init__(self, surface, start_x, start_y, vel_y):
        ShooterSprite.__init__(self, surface, start_x, start_y, 0, vel_y)
        
    def update(self):
        ShooterSprite.update(self)
        if self.y <= 0:
            self.kill()

class EnemySprite(ShooterSprite):
    def __init__(self, surface, start_x, vel_y):
        ShooterSprite.__init__(self, surface, start_x, 0, 0, vel_y)
        
    def update(self):
        ShooterSprite.update(self)
        if self.y >= 600:
            self.kill()
        
        
pygame.init()
screen = pygame.display.set_mode((500, 600))

background_group = pygame.sprite.RenderUpdates()
ship_group = pygame.sprite.RenderUpdates()
friendly_bullet_group = pygame.sprite.RenderUpdates()
enemy_group = pygame.sprite.RenderUpdates()

ship = ShipSprite(ship_surface, screen.get_width()/2, screen.get_height()-40)

ship_group.add(ship)
game_running = True

ship_vel = 0.5
while game_running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_running = False
            if event.key == K_LEFT:
                ship.vel_x += -ship_vel
            if event.key == K_RIGHT:
                ship.vel_x += ship_vel
            if event.key == K_SPACE:
                bullet_x = ship.rect.x+12
                bullet_y = ship.rect.y-20
                new_bullet = BulletSprite(bullet_surface, 
                                          bullet_x, bullet_y, -0.8)
                friendly_bullet_group.add(new_bullet)
        if event.type == KEYUP:
            if event.key == K_LEFT:
                ship.vel_x -= -ship_vel
            if event.key == K_RIGHT:
                ship.vel_x -= ship_vel

    if randint(0,100) == 1:
        star_speed = uniform(0.1, 0.5)
        star_x_location = randint(0,screen.get_width())
        new_star = StarSprite(star_surface, star_x_location, star_speed)
        background_group.add(new_star)

    if randint(0,2000) == 1:
        enemy_speed = uniform(0.2, 0.5)
        enemy_x_location = randint(0,screen.get_width())
        new_enemy = EnemySprite(enemy_surface, enemy_x_location, enemy_speed)
        enemy_group.add(new_enemy)

    screen.fill((0,0,0))
    
    update_rects = []
    groups = [background_group, ship_group, friendly_bullet_group, enemy_group]
    for g in groups:
        g.update()
        
    bullet_hit_list = []
    for bullet in friendly_bullet_group:
        bullet_hit = pygame.sprite.spritecollide(bullet, enemy_group, True)
        if bullet_hit != []:
            bullet_hit_list += bullet_hit
            bullet.kill()

    for g in groups:
        update_rects += g.draw(screen)
    pygame.display.update(update_rects)


