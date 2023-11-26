from abc import ABC, abstractmethod
import pygame
import os
from data.components.support import import_folder
from data.components.settings import Settings

class Creature(pygame.sprite.Sprite, ABC):
    def __init__(self, name, position, groups):
        super().__init__(groups)
        self.name = name
        self.info = getattr(Settings(), self.name)

        #health
        self.max_hp = self.info.get('health')
        self.hp = self.info.get('health')
        
        # movement
        self.normal_speed = self.info.get('speed')
        self.speed = self.info.get('speed')

        # atributos mais subjetivos
        self.position = position
        self.direction = pygame.math.Vector2()
    
        # invincibility
        self.invincible = False
        self.invincible_time = 0
        self.invincible_cooldown = 400

        # animate
        self.frame_index = 0
        self.animation_speed = 0.15
        self.status = "down"

        self.import_assets()
    

    def import_assets(self):
        path = os.path.dirname(os.path.abspath(__file__))+ Settings().creatures_folder + self.name

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
        
    def move(self, obstacle_sprites):
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
        self.colision('horizontal', obstacle_sprites)

        # vertical
        self.hitbox.y += self.direction.y * self.speed
        self.colision('vertical', obstacle_sprites)

        self.rect.center = self.hitbox.center

    def colision(self, direction, obstacle_sprites):
        # colision horizontal
        if direction == 'horizontal':
            for sprite in obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0 :
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0 :
                        self.hitbox.left = sprite.hitbox.right
        
        # colision vertical
        if direction == 'vertical':
            for sprite in obstacle_sprites:
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
