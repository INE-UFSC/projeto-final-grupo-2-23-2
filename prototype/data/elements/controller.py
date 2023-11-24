import pygame
import os
from data.components.sprites import Sprites
from data.elements.raid import Raid
from data.elements.guard import Guard
from data.elements.dash import Dash

class Controller:
    def __init__(self, level_name):
        self.player = None
        self.enemies = None
        
        self.level_name = level_name
        
        self.visible_sprites = Sprites(self.level_name)
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
                                    target_sprite.take_damage(self.player.inventory.get("raid").damage)
                                    
    def player_collect_item(self):
        for item_sprite in self.item_sprites:
            collision_sprites = pygame.sprite.spritecollide(item_sprite,self.player_sprite, False)
            if collision_sprites and self.player.picking:
                if 'raid' == item_sprite.sprite_type:
                    self.player.inventory.add_item(Raid(item_sprite.sprite_type, self.player,[]))
                if 'guard' == item_sprite.sprite_type:
                    self.player.inventory.add_item(Guard(item_sprite.sprite_type, self.player,[]))
                if 'dash' == item_sprite.sprite_type: 
                    self.player.inventory.add_item(Dash(item_sprite.sprite_type, self.player,[]))
                   
                item_sprite.kill()

    def player_defense_logic(self):
        if self.deffense_sprites:
            enemy_sprites = [sprite for sprite in self.attackable_sprites if hasattr(sprite, 'name') and sprite.name == 'enemy']
            for defense_sprite in self.deffense_sprites:
                collision_sprites = pygame.sprite.spritecollide(defense_sprite, enemy_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        target_sprite.can_attack = False


    def player_cooldowns(self):
        cd = self.player.cooldowns()
        if cd[0] == True:
            self.destroy_attack()
        if cd[1] == True:
            self.destroy_defense()

            
    def update_player(self, player, inventory):
        self.player = player
        self.player.inventory = inventory
        for item in self.player.inventory.items:
            item.player = self.player

