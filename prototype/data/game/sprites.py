from data.utils.settings import Settings
import pygame
import os

# all visible sprites + custom_draw pelo y
class Sprites(pygame.sprite.Group):
    def __init__(self, level_name):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.half_width = self.surface.get_size()[0] // 2
        self.half_heigth = self.surface.get_size()[1] // 2
        image = os.path.dirname(os.path.abspath(__file__))+Settings().levels_folder + level_name + '/map.png'
        self.floor_surface = pygame.image.load(image).convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))
        # desvia o map em referencia a tela
        self.offset = pygame.math.Vector2( )

    # praticamente um draw()
    def custom_draw(self, player):
        self.player = player

        # calculando offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_heigth

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.surface.blit(self.floor_surface,floor_offset_pos)

        # desenhando
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.surface.blit(sprite.image, offset_position)
            
    def enemy_update(self,player, visible_sprites):
        enemies_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']

        for enemy in enemies_sprites:
            enemy.enemy_update(player, visible_sprites)
