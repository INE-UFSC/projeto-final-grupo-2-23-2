from data.utils.settings import Settings
from data.game.creature import Creature
from data.game.player import Player
from data.utils.support import import_folder

import pygame
import os

class Enemy(Creature):
    def __init__(self, name, position, groups):
        super().__init__(name, position, groups)

        self.__image = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + Settings().creatures_folder + self.name + '/' +  self.name + '.png').convert_alpha()
        self.__rect = self.__image.get_rect(topleft=position)
        self.__hitbox = self.__rect.inflate(0, -10)
        
        self.__state = 'idle'
        self.__sprite_type = 'enemy'
        self.__origin = position
        
        #attack
        self.__detect_range = self.info.get('detect_range')
        self.__attack_range = self.info.get('attack_range')
        self.__attack_cooldown = self.info.get('attack_cooldown')
        self.__attack_damage = self.info.get('attack_damage')

        self.__attacking = False
        self.__can_damage = True
        self.__attack_time = 0

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value):
        self.__rect = value

    @property
    def hitbox(self):
        return self.__hitbox

    @hitbox.setter
    def hitbox(self, value):
        self.__hitbox = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def sprite_type(self):
        return self.__sprite_type

    @sprite_type.setter
    def sprite_type(self, value):
        self.__sprite_type = value

    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, value):
        self.__origin = value

    @property
    def detect_range(self):
        return self.__detect_range

    @detect_range.setter
    def detect_range(self, value):
        self.__detect_range = value

    @property
    def attack_range(self):
        return self.__attack_range

    @attack_range.setter
    def attack_range(self, value):
        self.__attack_range = value

    @property
    def attack_cooldown(self):
        return self.__attack_cooldown

    @attack_cooldown.setter
    def attack_cooldown(self, value):
        self.__attack_cooldown = value

    @property
    def attack_damage(self):
        return self.__attack_damage

    @attack_damage.setter
    def attack_damage(self, value):
        self.__attack_damage = value

    @property
    def attacking(self):
        return self.__attacking

    @attacking.setter
    def attacking(self, value):
        self.__attacking = value

    @property
    def can_damage(self):
        return self.__can_damage

    @can_damage.setter
    def can_damage(self, value):
        self.__can_damage = value

    @property
    def attack_time(self):
        return self.__attack_time

    @attack_time.setter
    def attack_time(self, value):
        self.__attack_time = value

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not "_" in self.status:
                self.status = self.status + "_idle"

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not "attack" in self.status:
                splited_status = self.status.split("_")
                if len(splited_status) == 1:
                    self.status = self.status + "_attack"
                else:
                    splited_status[1] = "attack"
                    self.status = "_".join(splited_status)

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)
    
    def return_to_origin(self):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        origin_vec = pygame.math.Vector2(self.origin)
        distance = (origin_vec - enemy_vec).magnitude()
        if distance > 0:
            direction = (origin_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)
        
    def get_state(self, player):
        distance_to_player = self.get_player_distance_direction(player)[0]
        distance_to_origin = self.return_to_origin()[0]
        
        if distance_to_player <= self.attack_range:
            self.state = 'attack'

        elif distance_to_player <= self.detect_range:
            self.state = 'move'
        else:
            if distance_to_origin >= 10:
                self.state = 'return'
            else:
                self.state = 'idle'

    def action(self, player):
        if self.invincible:
                self.direction = self.get_player_distance_direction(player)[1]*(-1)
        else:
            if self.state == 'attack' and self.cooldowns() and self.can_damage:
                self.direction = pygame.math.Vector2()
                self.attack(player)
            
            elif self.state == 'move':
                    self.direction = self.get_player_distance_direction(player)[1]
            
            elif self.state == 'return':
                    self.direction = self.return_to_origin()[1]
            
            else:
                self.direction = pygame.math.Vector2()

    def attack(self, player: Player):
        player.take_damage(self.attack_damage)
        self.attacking = True
        self.attack_time = pygame.time.get_ticks()

    def enemy_update(self, player, visible_sprites):
        self.get_state(player)
        self.action(player)
        self.show_health_bar(visible_sprites)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.status = self.status.split("_")[0]
        if self.invincible:
            if current_time - self.invincible_time >= self.invincible_cooldown:
                self.invincible = False
        else:
            return True
    
    def take_damage(self, amount):
        if self.invincible == False:
            self.hp -= amount
            self.invincible = True
            self.invincible_time = pygame.time.get_ticks()

            if self.hp <= 0:
                self.kill()

    def show_health_bar(self,visible_sprites):
        # coordinarion calculation
        width = self.rect.width*1.5
        # coordinarion calculation (continuation)
        x = self.rect.topleft[0] - visible_sprites.player.rect.centerx + visible_sprites.half_width - (width - self.rect.width) / 2
        y = self.rect.topleft[1] - visible_sprites.player.rect.centery + visible_sprites.half_height - 20
        self.desvio_y = self.rect.centery - visible_sprites.half_height

        # bg rect
        bg_rect = pygame.Rect(x, y, self.rect.width * 1.5, 12)
        pygame.draw.rect(visible_sprites.surface, "#222222", bg_rect)

        # insider rect
        ratio = self.hp / self.max_hp
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(visible_sprites.surface, "red", current_rect)
        pygame.draw.rect(visible_sprites.surface, "#111111", bg_rect, 3)

    def update(self, obstacle_sprites):
        self.get_status()
        self.animate()
        self.move(obstacle_sprites)
        self.cooldowns()

