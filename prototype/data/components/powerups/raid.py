from data.components.powerups.powerup import Powerup
import pygame
import os

class Raid(Powerup):
    def __init__(self, name, player, groups):
        super().__init__(name, player, groups)

        self.damage = 40
        self.duration = 170
        self.cooldown = 400
        self.time = None
        
        if "right" in self.direction:
            self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/../../../resources/graphics/ingame_graphics/items/weapons/sword/right.png').convert_alpha()
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
            
        elif 'left' in self.direction:
            self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/../../../resources/graphics/ingame_graphics/items/weapons/sword/left.png').convert_alpha()
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16))

        elif "down" in self.direction:
            self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/../../../resources/graphics/ingame_graphics/items/weapons/sword/down.png').convert_alpha()
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0))
            
        elif "up" in self.direction:
            self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/../../../resources/graphics/ingame_graphics/items/weapons/sword/up.png').convert_alpha()
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10,0))