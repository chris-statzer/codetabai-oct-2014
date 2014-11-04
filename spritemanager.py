from random import uniform, randint

import pygame
from pygame.locals import *

from spritesheet import SpriteSheet
from shootersprite import ShooterSprite


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


class PingPongEnemySprite(EnemySprite):
    def __init__(self, surface, start_x, vel_y, width):
        EnemySprite.__init__(self, surface, start_x, vel_y)
        self.vel_x = uniform(-0.4, 0.4)
        self.screen_width = width
        
    def update(self):
        EnemySprite.update(self)
        if self.x >= self.screen_width - 34:
            self.vel_x = -0.4
        if self.x <= 0:
            self.vel_x = 0.4
        

class ExplodeSprite(ShooterSprite):
    def __init__(self, surface, start_x, start_y):
        velocity = 2
        x_vel, y_vel = uniform(-velocity, velocity), uniform(-velocity, velocity)
        ShooterSprite.__init__(self, surface, start_x, start_y, x_vel, y_vel)
        self.lifetime = 300
        self.created_time = self.last_time
        
    def update(self):
        ShooterSprite.update(self)
        if  self.last_time >= self.created_time + self.lifetime:
            self.kill()


class SpriteManager(object):
    def __init__(self, sheet_json_file):
        self.sheet = SpriteSheet(sheet_json_file)
        self.groups = {}
        for g in ['background', 'friendly', 'enemy', 'particle', 'ui']:
            self.groups[g] = pygame.sprite.RenderUpdates()
        self.screen = pygame.display.get_surface()
        
    def add_star(self):
        star_speed = uniform(0.1, 0.5)
        star_x_location = randint(0,self.screen.get_width())
        star_surface = self.sheet.new_surface('star_y_1')
        new_star = StarSprite(star_surface, star_x_location, star_speed)
        self.groups['background'].add(new_star)
        return new_star
                
    def add_ship(self):
        ship_surface = self.sheet.new_surface('ship')
        new_ship = ShipSprite(ship_surface, 
            self.screen.get_width()/2, 
            self.screen.get_height()-40)
        self.groups['friendly'].add(new_ship)
        return new_ship
    
    def add_bullet(self, bullet_x, bullet_y):
        bullet_surface = self.sheet.new_surface('bullet')
        new_bullet = BulletSprite(bullet_surface, 
                                          bullet_x, bullet_y, -0.8)
        self.groups['friendly'].add(new_bullet)
        return new_bullet
                
    def add_random_enemy(self):
        enemy_speed = uniform(0.2, 0.5)
        enemy_x_location = randint(0, self.screen.get_width())
        if randint(1,2) == 1:
            enemy_surface = self.sheet.new_surface('enemy_1')
            new_enemy = EnemySprite(enemy_surface, enemy_x_location, enemy_speed)
        else:
            enemy_surface = self.sheet.new_surface('enemy_2')
            new_enemy = PingPongEnemySprite(enemy_surface, enemy_x_location, enemy_speed, self.screen.get_width())
        self.groups['enemy'].add(new_enemy)
        return new_enemy
            
    def add_explosion(self, start_x, start_y):
        explode_image = 'explode_{}'.format(randint(1,2))
        explode_surface = self.sheet.new_surface(explode_image)
        new_explode = ExplodeSprite(explode_surface, start_x, start_y)
        self.groups['particle'].add(new_explode)
        return new_explode


