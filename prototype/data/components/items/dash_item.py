from data.components.items.item import Item
import pygame

class DashItem(Item):
    def __init__(self, player, groups):
        super().__init__(player, groups)

        self.time = None
        self.duration = 250
        self.cooldown = 500
        self.speed = 2 * self.player.speed
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