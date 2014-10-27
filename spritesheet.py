import json

import pygame

class SpriteSheet(object):
    def __init__(self, json_file):
        self._sub_rects = {}
        with open(json_file) as file_object:
            file_buffer = file_object.read()
            dumped_json = json.loads(file_buffer)
            self._image_file = dumped_json['image_file']
            for key, value in dumped_json['sub_rects'].items():
                self.define_sprite(key, tuple(value))
        self._sheet_surface = pygame.image.load(self._image_file)

    def define_sprite(self, sprite_key, sub_rect):
        self._sub_rects[sprite_key] = sub_rect

    def new_sprite(self, sprite_key):
        sprite_area = self._sub_rects[sprite_key]
        created_sprite = pygame.sprite.Sprite()
        created_sprite.image = \
            pygame.surface.Surface([sprite_area[2], sprite_area[3]])
        created_sprite.rect = created_sprite.image.get_rect()
        created_sprite.image.blit(self._sheet_surface, (0,0,0,0), sprite_area)
        return created_sprite


if __name__ == '__main__':
    from pygame.locals import *
    pygame.init()
    ss = SpriteSheet('bling.sht')
    sp = ss.new_sprite('ship')
    sp.rect.x = 100
    sp.rect.y = 100
    sg = pygame.sprite.Group()
    sg.add(sp, ss.new_sprite('star'))
    screen = pygame.display.set_mode((700, 800))
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_running = False
        screen.fill((0, 0, 0))
        sg.draw(screen)
        pygame.display.flip()

    print sg, sp



