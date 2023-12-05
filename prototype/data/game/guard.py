from data.utils.settings import Settings
from data.game.powerup import Powerup
import pygame


class Guard(Powerup):
    def __init__(self, name, player, groups):
        super().__init__(name, player, groups)
        self.__speed = 2
        self.__duration = self.info.get('duration')
        self.__cooldown = self.info.get('cooldown')
        self.__stamina_cost = 70

        if "right" in self.direction:
            self.__image = pygame.Surface((5, 40))
            self.__rect = self.__image.get_rect(midleft=player.rect.midright)
        elif 'left' in self.direction:
            self.__image = pygame.Surface((5, 40))
            self.__rect = self.__image.get_rect(midright=player.rect.midleft)
        elif "down" in self.direction:
            self.__image = pygame.Surface((40, 5))
            self.__rect = self.__image.get_rect(midtop=player.rect.midbottom)
        elif "up" in self.direction:
            self.__image = pygame.Surface((40, 5))
            self.__rect = self.__image.get_rect(midbottom=player.rect.midtop)

        self.__hitbox = self.__rect

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value

    @property
    def cooldown(self):
        return self.__cooldown

    @cooldown.setter
    def cooldown(self, value):
        self.__cooldown = value

    @property
    def stamina_cost(self):
        return self.__stamina_cost

    @stamina_cost.setter
    def stamina_cost(self, value):
        self.__stamina_cost = value

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value):
        self.__rect = value

    @property
    def hitbox(self):
        return self.__hitbox

    @hitbox.setter
    def hitbox(self, value):
        self.__hitbox = value