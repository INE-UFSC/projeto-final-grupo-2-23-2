from data.utils.settings import Settings
from data.game.powerup import Powerup
import pygame

class Dash(Powerup):
    def __init__(self, name, player, groups):
        super().__init__(name, player, groups)

        self.__stamina_cost = 30
        self.__duration = self.info.get('duration')
        self.__cooldown = self.info.get('cooldown')
        self.__speed = self.info.get('speed')
        self.__direction = pygame.math.Vector2()

    @property
    def stamina_cost(self):
        return self.__stamina_cost

    @stamina_cost.setter
    def stamina_cost(self, value):
        self.__stamina_cost = value

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
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    def get_player_direction(self):
        if self.player.direction.magnitude() != 0:
            self.direction = self.player.direction
        else:
            if "down" in self.player.status:
                self.direction.x = 0
                self.direction.y = 1
            elif "up" in self.player.status:
                self.direction.x = 0
                self.direction.y = -1
            elif "left" in self.player.status:
                self.direction.x = -1
                self.direction.y = 0
            elif 'right' in self.player.status:
                self.direction.x = 1
                self.direction.y = 0
