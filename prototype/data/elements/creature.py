from abc import ABC, abstractmethod
import pygame
import os
from data.elements.inventory import Inventory
from data.components.support import import_folder

class Creature(pygame.sprite.Sprite, ABC):
    def __init__(self, name, hp, position, groups, obstacle_sprites):
        super().__init__(groups)

        # atributos concretos
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.speed = 3
        self.inventory = Inventory()

        # atributos mais subjetivos
        self.position = position
        # vetor direcao
        self.direction = pygame.math.Vector2()
        self.obstacle_sprites = obstacle_sprites
        
        self.attacking = False

        self.invincible = False
        self.invincible_time = None
        self.invincible_cooldown = 400

        # animate
        self.frame_index = 0
        self.animation_speed = 0.15

        self.status = "down"

        self.import_assets()
    
    def import_assets(self):
        path = os.path.dirname(os.path.abspath(__file__))+'/../../resources/elements/creatures/' + self.name

        animations = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        self.animations = {animation: [] for animation in animations}

        for animation in self.animations.keys():
            full_path = path + "/" + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= (len(animation)):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.hitbox = self.rect.inflate(0, -26)

        self.rect = self.image.get_rect(center = self.hitbox.center)
        
    def move(self):
        if abs(self.direction.y) > abs(self.direction.x):
            if self.direction.y > 0:
                self.status = "down"
            elif self.direction.y < 0:
                self.status = "up"
        else:
            if self.direction.x < 0:
                self.status = "left"
            elif self.direction.x > 0:
                self.status = "right"

        # diagonal fixed
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        # horizontal
        self.hitbox.x += self.direction.x * self.speed
        self.colision('horizontal')

        # vertical
        self.hitbox.y += self.direction.y * self.speed
        self.colision('vertical')

        self.rect.center = self.hitbox.center

    def colision(self, direction):
        # colision horizontal
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0 :
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0 :
                        self.hitbox.left = sprite.hitbox.right
        # colision vertical
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0 :
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0 :
                        self.hitbox.top = sprite.hitbox.bottom
        
    def take_damage(self, amount):
        if self.invincible == False:
            self.invincible = True
            self.invincible_time = pygame.time.get_ticks()
            
            if self.hp > 0:
                self.hp -= amount
            if self.hp < 0:
                self.hp = 0
        
    def heal(self, amount):
        if self.hp < self.max_hp:
            self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp 

    @abstractmethod
    def update(self):
        pass
