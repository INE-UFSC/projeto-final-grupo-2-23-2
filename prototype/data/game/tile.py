import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups, sprite_type, surface=pygame.Surface((64, 64))):
        super().__init__(groups)
        self.__sprite_type = sprite_type
        self.__image = surface

        if sprite_type == 'object':
            self.__rect = self.image.get_rect(topleft=(position[0], position[1] - 64))
        else:
            self.__rect = self.image.get_rect(topleft=position)

        self.__hitbox = self.__rect.inflate(0, -10)

    # Getters
    @property
    def sprite_type(self):
        return self.__sprite_type

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    @property
    def hitbox(self):
        return self.__hitbox

    # Setters
    @sprite_type.setter
    def sprite_type(self, value):
        self.__sprite_type = value

    @image.setter
    def image(self, value):
        self.__image = value

    @rect.setter
    def rect(self, value):
        self.__rect = value

    @hitbox.setter
    def hitbox(self, value):
        self.__hitbox = value
