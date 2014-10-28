

from random import randint

import pygame
from pygame.locals import *

from spritesheet import SpriteSheet


pygame.init()
screen = pygame.display.set_mode((500, 600))

sprite_sheet = SpriteSheet('assets/shooter_sheet.sheet')
star_surface = sprite_sheet.new_surface('star_y_1')

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
        
background_group = pygame.sprite.RenderUpdates()

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_running = False
                
    if randint(0,100) == 1:
        star_speed = randint(300,400)
        star_y_location = randint(0,screen.get_width())
        new_star = Star(star_surface, star_speed, star_y_location)
        background_group.add(new_star)
                
    screen.fill((0,0,0))
    background_group.update()                
    updated_rects = background_group.draw(screen)
    pygame.display.update(updated_rects)


