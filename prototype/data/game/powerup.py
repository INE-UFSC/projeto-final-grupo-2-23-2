from data.utils.settings import Settings
import pygame
import os

class Powerup(pygame.sprite.Sprite):
    def __init__(self, name, player, groups):
        super().__init__(groups)
        self.__time = 0
        self.__name = name
        self.__icon = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + Settings().icons_folder + self.name + '.png').convert_alpha()
        self.__player = player
        self.__direction = self.player.status
        self.__info = getattr(Settings(), self.name)

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, value):
        self.__icon = value

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, value):
        self.__player = value

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, value):
        self.__info = value
