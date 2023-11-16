from data.components.items.item import Item
import pygame

class OffensiveItem(Item):
    def __init__(self, player, groups):
        super().__init__(player, groups)
        direction = player.status

        self.damage = 40
        self.duration = 150
        self.cooldown = 400
        self.time = None
        
        if "right" in direction:
            self.image = pygame.Surface((40,20))
            self.rect = self.image.get_rect(midleft = player.rect.midright)
            
        elif 'left' in direction:
            self.image = pygame.Surface((40,20))
            self.rect = self.image.get_rect(midright = player.rect.midleft)

        elif "down" in direction:
            self.image = pygame.Surface((20,40))
            self.rect = self.image.get_rect(midtop = player.rect.midbottom)
            
        elif "up" in direction:
            self.image = pygame.Surface((20,40))
            self.rect = self.image.get_rect(midbottom = player.rect.midtop)