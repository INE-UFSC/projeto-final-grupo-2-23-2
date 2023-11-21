from abc import ABC, abstractmethod
import pygame
import os
from data.components.creatures.inventory import Inventory
from data.components.creatures.support import import_folder

#a

class Creature(pygame.sprite.Sprite, ABC):
    def __init__(self, name, hp, position, groups, obstacle_sprites):
        # insanciacao do Sprite
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
    
    def import_assets(self):
        path = os.path.dirname(os.path.abspath(__file__))+'/../../../resources/graphics/ingame_graphics/' + self.name 
        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [],
            'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
            'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': [],
            'up_dash': [], 'down_dash': [], 'left_dash': [], 'right_dash': [],
            'up_deffend': [], 'down_deffend': [], 'left_deffend': [], 'right_deffend': []
        }
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
        # normalizando a velocidade na diagonal
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
