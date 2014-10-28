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
        print 'Loaded: ', json_file
        self._sheet_surface = pygame.image.load(self._image_file)
        print 'Loaded: ', self._image_file
        

    def define_sprite(self, sprite_key, sub_rect):
        self._sub_rects[sprite_key] = sub_rect

    def new_surface(self, sprite_key):
        sprite_area = self._sub_rects[sprite_key]
        new_surface = pygame.surface.Surface([sprite_area[2], sprite_area[3]])
        new_surface.blit(self._sheet_surface, (0,0,0,0), sprite_area)
        return new_surface

