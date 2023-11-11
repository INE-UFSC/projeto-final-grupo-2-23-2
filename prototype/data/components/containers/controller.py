import pygame
import os
from data.components.containers.tiles.y_camera_group import YSortCameraGroup
from data.components.items.offensive_item import OffensiveItem

class Controller:
    def __init__(self):
        self.__player = None
        self.__enemies = None
        
        self.__visible_sprites = YSortCameraGroup()
        self.__obstacles_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        self.attacks_sprites = pygame.sprite.Group()
        self.item_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
        
        self.current_attack = None
        
        
    def create_attack(self):
        self.current_attack = OffensiveItem(self.player,[self.visible_sprites,self.attacks_sprites])
        
    def destroy_attack(self):
        if self.current_attack != None:
            self.current_attack.kill()
            self.current_attack = None

    def player_attack_logic(self):
        if self.attacks_sprites:
            for sprites_ataque in self.attacks_sprites:
                collision_sprites = pygame.sprite.spritecollide(sprites_ataque,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                            if target_sprite.hp == 0:
                                target_sprite.kill()
                            else:
                                if target_sprite.invincible == False:
                                    target_sprite.take_damage(self.player.damage)
                                
    def player_collect_item(self):
        for item_sprite in self.item_sprites:
            collision_sprites = pygame.sprite.spritecollide(item_sprite,self.player_sprite, False)
            if collision_sprites and self.player.picking:
                self.player.item_inventory.add_item(item_sprite)
                item_sprite.kill()
    
    @property
    def visible_sprites(self):
        return self.__visible_sprites

    @visible_sprites.setter
    def visible_sprites(self, visible_sprites):
        self.__visible_sprites = visible_sprites

    @property
    def obstacles_sprites(self):
        return self.__obstacles_sprites

    @obstacles_sprites.setter
    def obstacles_sprites(self, obstacles_sprites):
        self.__obstacles_sprites = obstacles_sprites
        
    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        self.__player = player

    @property
    def enemies(self):
        return self.__enemies

    @enemies.setter
    def enemies(self, enemies):
        self.__enemies = enemies