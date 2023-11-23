from data.elements.creature import Creature
from data.elements.player import Player
from data.components.support import import_folder
import pygame
import os

class Enemy(Creature):
    def __init__(self, name, hp, position, groups, visible_sprites, obstacle_sprites):
        super().__init__(name, hp, position, groups, obstacle_sprites)

        self.image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__))+'/../../resources/elements/enemies/enemy/' +  name + '.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -10)
        self.status = 'idle'
        self.range = 300
        self.sprite_type = 'enemy'
        self.speed = 3
        self.attack_range = 50
        self.damage = 25
        self.visible_sprites = visible_sprites

        self.can_damage = True
        self.attack_time = None
        self.attack_cooldown = 1000
        self.origin = position
        self.returning = False
        
        #barra de hp
        self.health_bar_size = self.rect.width*1.5
        self.ratio_health_bar = hp / self.health_bar_size # tamanho da barra
        self.import_assets()
        
    def import_assets(self):
        path = os.path.dirname(os.path.abspath(__file__))+'/../../resources/elements/enemies' + self.name 
        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [],
            'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
            'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': []
            }
        for animation in self.animations.keys():
            full_path = path + "/" + animation
            self.animations[animation] = import_folder(full_path)
        
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
            self.status += '_attack'

        elif distance_to_player <= self.range:
            self.status += '_move'
        else:
            if distance_to_origin >= 10:
                self.returning = 'return'
            else:
                self.status = 'idle'

    def action(self, player):
        if self.invincible:
                self.direction = self.get_player_distance_direction(player)[1]*(-1)
        else:
            if self.status == 'attack' and self.cooldowns() and self.can_damage:
                self.direction = pygame.math.Vector2()
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
    
    def show_health_bar(self):
        # coordinarion calculation
        x = self.rect.topleft[0] - self.visible_sprites.player.rect.centerx + self.visible_sprites.half_width - (self.health_bar_size-self.rect.width)/2
        y = self.rect.topleft[1] - self.visible_sprites.player.rect.centery + self.visible_sprites.half_heigth - 20
        self.desvio_y = self.rect.centery - self.visible_sprites.half_heigth

        # bg rect
        bg_rect = pygame.Rect(x, y, self.rect.width*1.5, 12) 
        pygame.draw.rect(self.visible_sprites.surface, "#222222", bg_rect) 

        # insider rect
        ratio = self.hp / self.max_hp
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.visible_sprites.surface, "red", current_rect)
        pygame.draw.rect(self.visible_sprites.surface, "#111111", bg_rect, 3)

    def update(self):
        self.show_health_bar()
        self.move()
        self.cooldowns()

