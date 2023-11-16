import pygame
import os
from data.components.containers.tiles.y_camera_group import YSortCameraGroup
from data.components.powerups.raid import Raid
from data.components.powerups.guard import Guard
from data.components.powerups.dash import Dash

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
        self.current_attack = Raid("raid", self.player,[self.visible_sprites,self.attacks_sprites])
        
    def destroy_attack(self):
        if self.current_attack != None:
            self.current_attack.kill()
            self.current_attack = None
            # self.player.attacking = False

    def create_defense(self):
        self.current_defense = Guard("guard",self.player,[self.visible_sprites,self.deffense_sprites, self.obstacles_sprites])
        
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
                                    target_sprite.take_damage(self.player.weapon.damage)
                                    
    def player_collect_item(self):
        for item_sprite in self.item_sprites:
            collision_sprites = pygame.sprite.spritecollide(item_sprite,self.player_sprite, False)
            if collision_sprites and self.player.picking:
                if 'weapon' in item_sprite.name:
                    object = Raid(item_sprite.name, self.player,[])
                    self.player.inventory.add_item(object)
                    self.player.weapon = object####
                if 'defensive' in item_sprite.name:
                    object = Guard(item_sprite.name, self.player,[])
                    self.player.inventory.add_item(object)
                    self.player.defense = object#####
                if 'dash' in item_sprite.name:
                    object = Dash(item_sprite.name, self.player,[])
                    self.player.dash = object
                    
                item_sprite.kill()

