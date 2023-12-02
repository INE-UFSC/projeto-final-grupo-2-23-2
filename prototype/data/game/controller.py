from data.utils.settings import Settings
from data.utils.audio import Audio
import pygame
import os
from data.game.sprites import Sprites

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

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update(self.obstacles_sprites)
        self.visible_sprites.enemy_update(self.player, self.visible_sprites)
        self.attack_collision()
        self.item_collision()