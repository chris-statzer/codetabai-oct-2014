import pygame


class ShooterSprite(pygame.sprite.Sprite):
    def __init__(self, surface, start_x, start_y, vel_x=0, vel_y=0):
        pygame.sprite.Sprite.__init__(self)
        self.last_time = pygame.time.get_ticks()
        self.image = surface
        self.rect = self.image.get_rect()
        self.x, self.y = (start_x, start_y)
        self.vel_x, self.vel_y = vel_x, vel_y
    
    def do_physics(self, delta_time):
        self.x += (self.vel_x * delta_time)
        self.y += (self.vel_y * delta_time)
        
    
    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = (current_time - self.last_time)
        #print delta_time, delta_time  * 0.001
        self.do_physics(delta_time)
        self.last_time = current_time
    
    def set_x(self, val):
        self._x = val
        self.rect.x = val

    def get_x(self):
        return self._x

    x = property(get_x, set_x)

    def set_y(self,val):
        self._y = val
        self.rect.y = val
    
    def get_y(self):
        return self._y

    y = property(get_y, set_y)
