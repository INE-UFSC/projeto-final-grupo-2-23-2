import pygame
import os
from data.components.containers.y_camera_group import YSortCameraGroup

class Controller:
    def __init__(self):
        self.__visible_sprites = YSortCameraGroup()
        self.__obstacles_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        self.attacks_sprites = pygame.sprite.Group()
        
    @property
    def visible_sprites(self):
        return self.__visible_sprites

    @visible_sprites.setter
    def visible_sprites(self, visible_sprites):
        self.__visible_sprites = visible_sprites

    @property
    def obstacles_sprites(self):
        return self.__obstacles_sprites

    @obstacles_sprites.setter
    def obstacles_sprites(self, obstacles_sprites):
        self.__obstacles_sprites = obstacles_sprites