import pygame
import os
from data.components.sprites import Sprites
from data.elements.raid import Raid
from data.elements.guard import Guard
from data.elements.dash import Dash

class Controller:
    def __init__(self):
        self.player = None
        self.enemies = None
        
        self.visible_sprites = Sprites()
        self.obstacles_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        self.attacks_sprites = pygame.sprite.Group()
        self.deffense_sprites = pygame.sprite.Group()
        self.item_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
        

    def attack_collision(self):
        if self.attacks_sprites:
            for attack_sprite in self.attacks_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                            target_sprite.take_damage(attack_sprite.damage)
                                    
    def item_collision(self):
        for item_sprite in self.item_sprites:
            collision_sprites = pygame.sprite.spritecollide(item_sprite,self.player_sprite, False)
            if collision_sprites:
                self.player.pick_item(item_sprite)

    def defense_collision(self):
        if self.deffense_sprites:
            enemy_sprites = [sprite for sprite in self.attackable_sprites if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
            for defense_sprite in self.deffense_sprites:
                collision_sprites = pygame.sprite.spritecollide(defense_sprite, enemy_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        target_sprite.can_attack = False

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.attack_collision()
        self.defense_collision()
        self.item_collision()