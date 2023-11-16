import pygame
import os
from data.components.containers.tiles.y_camera_group import YSortCameraGroup
from data.components.items.offensive_item import OffensiveItem
from data.components.items.defensive_item import DefensiveItem
from data.components.items.dash_item import DashItem

class Controller:
    def __init__(self):
        self.player = None
        self.enemies = None
        
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        self.attacks_sprites = pygame.sprite.Group()
        self.deffense_sprites = pygame.sprite.Group()
        self.item_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
        
        self.current_attack = None
        self.current_defense = None
        
        
    def create_attack(self):
        self.current_attack = OffensiveItem(self.player,[self.visible_sprites,self.attacks_sprites])
        
    def destroy_attack(self):
        if self.current_attack != None:
            self.current_attack.kill()
            self.current_attack = None
            # self.player.attacking = False

    def create_defense(self):
        self.current_defense = DefensiveItem(self.player,[self.visible_sprites,self.deffense_sprites])
        
    def destroy_defense(self):
        if self.current_defense != None:
            self.current_defense.kill()
            self.current_defense = None

    def player_attack_logic(self):
        if self.attacks_sprites:
            for attack_sprite in self.attacks_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                            if target_sprite.hp == 0:
                                target_sprite.kill()
                            else:
                                if target_sprite.invincible == False:
                                    target_sprite.take_damage(self.player.inventory.weapon.damage)
                                    
    def player_collect_item(self):
        for item_sprite in self.item_sprites:
            collision_sprites = pygame.sprite.spritecollide(item_sprite,self.player_sprite, False)
            if collision_sprites and self.player.picking:
                self.player.item_inventory.add_item(item_sprite.name)
                if 'weapon' in item_sprite.name:
                    self.player.inventory.weapon = OffensiveItem(self.player,[])
                if 'defensive' in item_sprite.name:
                    self.player.inventory.defense = DefensiveItem(self.player,[])
                if 'dash' in item_sprite.name:
                    self.player.inventory.dash = DashItem(self.player,[])
                    
                item_sprite.kill()

    def player_cooldowns(self):
        cd = self.player.cooldowns()
        if cd[0] == True:
            self.destroy_attack()
        if cd[1] == True:
            self.destroy_defense()