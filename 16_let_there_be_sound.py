from random import randint, uniform

import pygame
from pygame.locals import *

from spritemanager import SpriteManager

pygame.init()
screen = pygame.display.set_mode((500, 600))

sprite_mgr = SpriteManager('assets/shooter_sheet.sheet')
shoot_snd = pygame.mixer.Sound('assets/sounds/laser2.ogg')
explode_snd = pygame.mixer.Sound('assets/sounds/explosion2.ogg')

shoot_snd.set_volume(0.1)
explode_snd.set_volume(0.1)

ship = sprite_mgr.add_ship()

game_running = True

ship_vel = 0.4
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
                sprite_mgr.add_bullet(bullet_x, bullet_y)
                shoot_snd.play()
        if event.type == KEYUP:
            if event.key == K_LEFT:
                ship.vel_x -= -ship_vel
            if event.key == K_RIGHT:
                ship.vel_x -= ship_vel

    if randint(0,100) == 1:
        sprite_mgr.add_star()

    if randint(0,1000) == 1:
        sprite_mgr.add_random_enemy()

    screen.fill((0,0,0))
    
    update_rects = []
    groups = sprite_mgr.groups.values()
    
    for g in groups:
        g.update()
        
    bullet_hit_list = []
    for bullet in sprite_mgr.groups['friendly']:
        bullet_hit = pygame.sprite.spritecollide(bullet, sprite_mgr.groups['enemy'], True)
        if bullet_hit != []:
            bullet_hit_list += bullet_hit
            bullet.kill()
            explode_snd.play()
            for n in range(1,100):
                sprite_mgr.add_explosion(bullet.x, bullet.y)

    for g in groups:
        update_rects += g.draw(screen)
        
    if not ship.alive():
        ship = sprite_mgr.add_ship()
        
    pygame.display.update(update_rects)


