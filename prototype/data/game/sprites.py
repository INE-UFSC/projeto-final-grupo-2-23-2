from data.utils.settings import Settings
import pygame
import os

# all visible sprites + custom_draw pelo y
class Sprites(pygame.sprite.Group):
    def __init__(self, level_name):
        super().__init__()
        self.__surface = pygame.display.get_surface()
        self.__half_width = self.surface.get_size()[0] // 2
        self.__half_height = self.surface.get_size()[1] // 2
        image = os.path.dirname(os.path.abspath(__file__)) + Settings().levels_folder + level_name + '/map.png'
        self.__floor_surface = pygame.image.load(image).convert()
        self.__floor_rect = self.floor_surface.get_rect(topleft=(0, 0))
        # desvia o map em referencia a tela
        self.__offset = pygame.math.Vector2()

    # praticamente um draw()
    def custom_draw(self, player):
        self.player = player

        # calculando offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.__floor_rect.topleft - self.__offset
        self.__surface.blit(self.__floor_surface, floor_offset_pos)

        # desenhando
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.__offset
            self.__surface.blit(sprite.image, offset_position)

    def enemy_update(self, player, visible_sprites):
        enemies_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']

        for enemy in enemies_sprites:
            enemy.enemy_update(player, visible_sprites)

    # Getters
    @property
    def surface(self):
        return self.__surface

    @property
    def half_width(self):
        return self.__half_width

    @property
    def half_height(self):
        return self.__half_height

    @property
    def floor_surface(self):
        return self.__floor_surface

    @property
    def floor_rect(self):
        return self.__floor_rect

    @property
    def offset(self):
        return self.__offset

    # Setters
    @surface.setter
    def surface(self, value):
        self.__surface = value

    @half_width.setter
    def half_width(self, value):
        self.__half_width = value

    @half_height.setter
    def half_height(self, value):
        self.__half_height = value

    @floor_surface.setter
    def floor_surface(self, value):
        self.__floor_surface = value

    @floor_rect.setter
    def floor_rect(self, value):
        self.__floor_rect = value

    @offset.setter
    def offset(self, value):
        self.__offset = value
