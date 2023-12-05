from data.game.powerup import Powerup
import pygame
import os

class Raid(Powerup):
    def __init__(self, name, player, groups):
        super().__init__(name, player, groups)
        # self.damage = 40
        self.__stamina_cost = 50
        # self.duration = 170
        # self.cooldown = 400
        self.__damage = self.info.get('damage')
        self.__duration = self.info.get('duration')
        self.__cooldown = self.info.get('damage')

        if "right" in self.direction:
            self.__image = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + '/../../resources/elements/powerups/raid/right.png').convert_alpha()
            self.__rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(0, 16))

        elif 'left' in self.direction:
            self.__image = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + '/../../resources/elements/powerups/raid/left.png').convert_alpha()
            self.__rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0, 16))

        elif "down" in self.direction:
            self.__image = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + '/../../resources/elements/powerups/raid/down.png').convert_alpha()
            self.__rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-10, 0))

        elif "up" in self.direction:
            self.__image = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + '/../../resources/elements/powerups/raid/up.png').convert_alpha()
            self.__rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-10, 0))

    @property
    def stamina_cost(self):
        return self.__stamina_cost

    @stamina_cost.setter
    def stamina_cost(self, value):
        self.__stamina_cost = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

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
