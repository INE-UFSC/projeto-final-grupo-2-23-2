import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups, sprite_type, surface = pygame.Surface((64,64))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = (position[0], position[1] - 64))
        
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -10)