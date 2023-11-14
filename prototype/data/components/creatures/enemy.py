from data.components.creatures.creature import Creature
from data.components.creatures.player import Player
import pygame
import os

class Enemy(Creature):
    def __init__(self, name, hp, position, groups, visible_sprites, obstacle_sprites):
        super().__init__(name, hp, position, groups, visible_sprites, obstacle_sprites)

        self.__image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__))+'/../../../resources/graphics/enemies/' + name + '.png').convert_alpha()
        self.__rect = self.image.get_rect(topleft=position)
        self.__hitbox = self.__rect.inflate(0, -10)
        self.__status = 'idle'
        self.__range = 300
        self.__sprite_type = 'enemy'
        self.__speed = 2
        self.__attack_range = 50
        self.__damage = 10

        self.attacking = False
        self.attack_time = None
        self.attack_cooldown = 100
        
        self.invincible_time = None
        self.invincible_cooldown = 320

        self.origin = position
        
        #barra de hp
        self.health_bar_size = self.__rect.width*1.5
        self.ratio_health_bar = hp / self.health_bar_size # tamanho da barra
        
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
        

    def get_status(self, player):
        distance_to_player = self.get_player_distance_direction(player)[0]
        distance_to_origin = self.return_to_origin()[0]
        
        if distance_to_player <= self.attack_range:
            self.status = 'attack'

        elif distance_to_player <= self.range:
            self.status = 'move'
        else:
            if distance_to_origin != 0:
                self.status = 'return'
            else:
                self.status = 'idle'

    def action(self, player):
        if self.invincible:
                self.direction = self.get_player_distance_direction(player)[1]*(-1)
        else:
            if self.status == 'attack' and self.cooldowns():
                self.atacar(player)
            
            elif self.status == 'move':
                    self.direction = self.get_player_distance_direction(player)[1]
            
            elif self.status == 'return':
                    self.direction = self.return_to_origin()[1]
            
            else:
                self.direction = pygame.math.Vector2()

    def atacar(self, player: Player):
        player.take_damage(self.damage)
        self.attacking = True
        self.attack_time = pygame.time.get_ticks()

    def enemy_update(self, player):
        self.get_status(player)
        self.action(player)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
        if self.invincible:
            if current_time - self.invincible_time >= self.invincible_cooldown:
                self.invincible = False
        else:
            return True
        
    def update(self):
        self.health_bar()
        self.move()
        self.cooldowns()

#---------------------
# -Getters e Setters-
#---------------------

    @property
    def sprite_type(self):
        return self.__sprite_type
    
    @property
    def speed(self):
        return self.__speed
    
    @property
    def attack_range(self):
        return self.__attack_range
    
    @property
    def damage(self):
        return self.__damage
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, image):
        self.__image = image
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def range(self):
        return self.__range
    
    @range.setter
    def range(self, range):
        self.__range = range
        
    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def hitbox(self):
        return self.__hitbox
    
    @hitbox.setter
    def hitbox(self, hitbox):
        self.__hitbox = hitbox 

    # todo: gambiarra
    def health_bar(self):
        sv = self.visible_sprites
        a0 = self.rect.topleft[0] - sv.player.rect.centerx + sv.half_width - (self.health_bar_size-self.rect.width)/2
        a1 = self.rect.topleft[1] - sv.player.rect.centery + sv.half_heigth - 20
        self.desvio_y = self.rect.centery - sv.half_heigth

        pygame.draw.rect(sv.surface, (255, 0, 0), (a0, a1, self.hp/self.ratio_health_bar, 10))
        pygame.draw.rect(sv.surface, (255, 255, 255), (a0, a1, self.health_bar_size, 10),1)
