from data.utils.settings import Settings
from data.utils.audio import Audio
import pygame
import os
from data.game.sprites import Sprites

class Controller:
    def __init__(self, level_name):
        self.__player = None
        self.__enemies = None
        self.__level_name = level_name
        self.__visible_sprites = Sprites(self.__level_name)
        self.__obstacles_sprites = pygame.sprite.Group()
        self.__attackable_sprites = pygame.sprite.Group()
        self.__attacks_sprites = pygame.sprite.Group()
        self.__deffense_sprites = pygame.sprite.Group()
        self.__item_sprites = pygame.sprite.Group()
        self.__player_sprite = pygame.sprite.Group()

    # Getters e setters
    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, value):
        self.__player = value

    @property
    def enemies(self):
        return self.__enemies

    @enemies.setter
    def enemies(self, value):
        self.__enemies = value

    @property
    def level_name(self):
        return self.__level_name

    @level_name.setter
    def level_name(self, value):
        self.__level_name = value

    @property
    def visible_sprites(self):
        return self.__visible_sprites

    @property
    def obstacles_sprites(self):
        return self.__obstacles_sprites

    @property
    def attackable_sprites(self):
        return self.__attackable_sprites

    @property
    def attacks_sprites(self):
        return self.__attacks_sprites

    @property
    def deffense_sprites(self):
        return self.__deffense_sprites

    @property
    def item_sprites(self):
        return self.__item_sprites

    @property
    def player_sprite(self):
        return self.__player_sprite

    def attack_collision(self):
        if self.__attacks_sprites:
            for attack_sprite in self.__attacks_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.__attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        target_sprite.take_damage(attack_sprite.damage)

    def item_collision(self):
        for item_sprite in self.__item_sprites:
            collision_sprites = pygame.sprite.spritecollide(item_sprite, self.__player_sprite, False)
            if collision_sprites:
                self.__player.pick_item(item_sprite)

    def run(self):
        self.__visible_sprites.custom_draw(self.__player)
        self.__visible_sprites.update(self.__obstacles_sprites)
        self.__visible_sprites.enemy_update(self.__player, self.__visible_sprites)
        self.attack_collision()
        self.item_collision()
