from data.game.powerup import Powerup
import pygame
import os

class Raid(Powerup):
    def __init__(self, name, player, groups):
        super().__init__(name, player, groups)
#         self.damage = 40
        self.stamina_cost = 50
#         self.duration = 170
#         self.cooldown = 400
        self.damage = self.info.get('damage')
        self.duration = self.info.get('duration')
        self.cooldown = self.info.get('damage')
        
        if "right" in self.direction:
            self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/../../resources/elements/powerups/raid/right.png').convert_alpha()
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
            
        elif 'left' in self.direction:
            self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/../../resources/elements/powerups/raid/left.png').convert_alpha()
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16))

        elif "down" in self.direction:
            self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/../../resources/elements/powerups/raid/down.png').convert_alpha()
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0))
            
        elif "up" in self.direction:
            self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/../../resources/elements/powerups/raid/up.png').convert_alpha()
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10,0))