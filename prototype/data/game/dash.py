from data.utils.settings import Settings
from data.game.powerup import Powerup
import pygame

class Dash(Powerup):
    def __init__(self, name, player, groups):
        super().__init__(name, player, groups)

        self.stamina_cost = 30
        self.duration = self.info.get('duration')
        self.cooldown = self.info.get('cooldown')
        self.speed = self.info.get('speed')
        self.direction = pygame.math.Vector2()

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