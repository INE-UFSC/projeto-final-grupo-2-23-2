from abc import ABC, abstractmethod
import pygame
import os
from data.components.creatures.inventory import Inventory


class Creature(pygame.sprite.Sprite, ABC):
    def __init__(self, name, hp, position, groups, visible_sprites, obstacle_sprites):
        # insanciacao do Sprite
        super().__init__(groups)

        # atributos concretos
        self.__name = name
        self.__max_hp = hp
        self.__hp = hp
        self.__speed = 5
        self.__inventory = Inventory()

        # atributos mais subjetivos
        self.__position = position
        # vetor direcao
        self.__direction = pygame.math.Vector2()
        self.__visible_sprites = visible_sprites
        self.__obstacle_sprites = obstacle_sprites

    # getters e setters
    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp
    
    @property
    def max_hp(self):
        return self.__max_hp
    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, speed):
        self.__speed = speed
    
    @property
    def inventory(self):
        return self.__inventory
    
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @property
    def position(self):
        return self.__position
    
    @property
    def obstacle_sprites(self):
        return self.__obstacle_sprites
    
    @property
    def visible_sprites(self):
        return self.__visible_sprites
    
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
        if self.hp > 0:
            self.hp -= amount
        if self.hp < 0:
            self.hp = 0
    
    def heal(self, amount):
        if self.hp < self.max_hp:
            self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp 

    # todo
    def attack(self):
        self.__offensive_item.attack()
    # todo?
    def deffend(self):
        self.__defensive_item.deffend()
    
    @abstractmethod
    def update(self):
        pass
