from abc import ABC, abstractmethod
import pygame
import os
from data.utils.support import import_folder
from data.utils.settings import Settings

class Creature(pygame.sprite.Sprite, ABC):
    def __init__(self, name, position, groups):
        self.__name = name
        self.__info = getattr(Settings(), self.__name)
        self.__max_hp = self.__info.get('health')
        self.__hp = self.__info.get('health')
        self.__normal_speed = self.__info.get('speed')
        self.__speed = self.__info.get('speed')
        self.__direction = pygame.math.Vector2()
        self.__invincible = False
        self.__invincible_time = 0
        self.__invincible_cooldown = 400
        self.__frame_index = 0
        self.__animation_speed = 0.15
        self.__status = "down"

        self.generate(groups, position)
        self.import_assets()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def max_hp(self):
        return self.__max_hp

    @max_hp.setter
    def max_hp(self, value):
        self.__max_hp = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def normal_speed(self):
        return self.__normal_speed

    @normal_speed.setter
    def normal_speed(self, value):
        self.__normal_speed = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    @property
    def invincible(self):
        return self.__invincible

    @invincible.setter
    def invincible(self, value):
        self.__invincible = value

    @property
    def invincible_time(self):
        return self.__invincible_time

    @invincible_time.setter
    def invincible_time(self, value):
        self.__invincible_time = value

    @property
    def invincible_cooldown(self):
        return self.__invincible_cooldown

    @invincible_cooldown.setter
    def invincible_cooldown(self, value):
        self.__invincible_cooldown = value

    @property
    def frame_index(self):
        return self.__frame_index

    @frame_index.setter
    def frame_index(self, value):
        self.__frame_index = value

    @property
    def animation_speed(self):
        return self.__animation_speed

    @animation_speed.setter
    def animation_speed(self, value):
        self.__animation_speed = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def generate(self, groups, position):
        super().__init__(groups)
        self.position = position

    def import_assets(self):
        path = os.path.dirname(os.path.abspath(__file__)) + Settings().creatures_folder + self.name

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

        self.rect = self.image.get_rect(center=self.hitbox.center)

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
        self.collision('horizontal', obstacle_sprites)

        # vertical
        self.hitbox.y += self.direction.y * self.speed
        self.collision('vertical', obstacle_sprites)

        self.rect.center = self.hitbox.center

    def collision(self, direction, obstacle_sprites):
        # collision horizontal
        if direction == 'horizontal':
            for sprite in obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        # collision vertical
        if direction == 'vertical':
            for sprite in obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def take_damage(self, amount):
        if not self.invincible:
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
               