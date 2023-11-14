from data.components.creatures.creature import Creature
from data.components.creatures.inventory import Inventory
import pygame
import os
# from support import import_folder

class Player(Creature):
    def __init__(self, name, hp, position, groups, visible_sprites, obstacle_sprites, generate_attack, destroy_attack):
        super().__init__(name, hp, position, groups, visible_sprites, obstacle_sprites)
        
        # todo: analisar heranca inimigo jogador
        self.__name = name
        self.image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__))+'/../../../resources/graphics/player/' + name + '.png').convert_alpha()
        self.__rect = self.image.get_rect(topleft=position)
        self.__hitbox = self.__rect.inflate(0, -26)

        # movement 
        self.import_assets()
        self.status = 'down'
        self.direction = pygame.math.Vector2()
        self.moving = True
        
        self.weapon = None
        self.defense = None
        
        # attack
        self.attacking = False
        self.attack_time = None
        self.attack_cooldown = 150
        
        self.dashing = False
        self.dashing_time = None
        self.dashing_duration = 250
        self.dashing_cooldown = 500
        self.dashing_speed = 2 * self.speed
        self.dashing_direction = None
        
        self.invencible = False
        self.invincible_time = None
        self.invincible_cooldown = 500
        
        self.deffending = False

        self.picking = False
        
        self.item_inventory = Inventory()
        
        self.ratio_health_bar = hp / 200 # tamanho da barra
        self.damage = 40
        
        #metodos vindos de fase
        self.generate_attack = generate_attack
        self.destroy_attack = destroy_attack
        self.sprite_type = 'player'

    
    def import_assets(self):
        path = os.path.dirname(os.path.abspath(__file__))+'/../../../resources/graphics/player/' + self.name + '.png'
        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [],
            'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
            'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': [],
            'up_dash': [], 'down_dash': [], 'left_dash': [], 'right_dash': [],
            'up_deffend': [], 'down_deffend': [], 'left_deffend': [], 'right_deffend': [],
        }
        for animation in self.animations.keys():
            full_path = path + animation
            # self.animation[animation] = import_folder(full_path)

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

        if self.deffending:
            if not "deffend" in self.status:
                splited_status = self.status.split("_")
                if len(splited_status) == 1:
                    self.status = self.status + "_deffend"
                else:
                    splited_status[1] = "deffend"
                    self.status = "_".join(splited_status)

        if self.dashing:
            if not "dash" in self.status:
                splited_status = self.status.split("_")
                if len(splited_status) == 1:
                    self.status = self.status + "_dash"
                else:
                    splited_status[1] = "dash"
                    self.status = "_".join(splited_status)

    def input(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        
        # movement input
        if not self.dashing:
            if keys[pygame.K_UP] and self.moving:
                self.direction.y = -1   
                self.status = 'up'

            elif keys[pygame.K_DOWN] and self.moving:
                self.direction.y = 1  
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_LEFT] and self.moving:
                self.direction.x = -1
                self.status = 'left'

            elif keys[pygame.K_RIGHT] and self.moving:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0
        
        # attack input
        if keys[pygame.K_SPACE]:
            if (self.weapon is not None) and (not self.attacking):
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.generate_attack()
        
        # pick input
        if keys[pygame.K_c]:
            self.picking = True
        else:
            self.picking = False
        
        # deffend input
        if keys[pygame.K_LCTRL]:
            if self.defense is not None:
                self.moving = False
                self.invincible = True
                self.deffending = True
                self.invincible_time = pygame.time.get_ticks()


        # dash input 
        if keys[pygame.K_LSHIFT]:
            try:
                if current_time - self.dashing_time >= self.dashing_cooldown:
                    self.dash()
            except:
                self.dash()
            

    def update(self):
        self.input()
        self.get_status()
        self.cooldowns()
        self.move()
        self.health_bar()

    
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            self.moving = False
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.moving = True
                self.destroy_attack()
                self.status = self.status.split("_")[0]
                
        if self.invincible:
            if current_time - self.invincible_time >= self.invincible_cooldown:
                self.invincible = False
                self.deffending = False
                self.moving = True 
                self.status = self.status.split("_")[0]

        if self.dashing:
            self.speed = self.dashing_speed
            self.direction = self.dashing_direction
            
            if current_time - self.dashing_time >= self.dashing_duration:
                self.dashing = False
                self.invincible = False
                self.speed = self.dashing_speed / 2
            
                self.status = self.status.split("_")[0]

    
    def dash(self):
        if self.direction.magnitude() != 0:
            self.dashing_direction = self.direction
        else:
            if "down" in self.status:
                self.direction.x = 0
                self.direction.y = 1
            elif "up" in self.status:
                self.direction.x = 0
                self.direction.y = -1
            elif "left" in self.status:
                self.direction.x = -1
                self.direction.y = 0
            elif 'right' in self.status:
                self.direction.x = 1
                self.direction.y = 0
            
            self.dashing_direction = self.direction
        self.dashing_time = pygame.time.get_ticks()
        self.dashing = True
        self.invincible = True
        self.invincible_time = pygame.time.get_ticks()
    # gambiarra
    def health_bar(self):
        sv = self.visible_sprites
        pygame.draw.rect(sv.surface, (255, 0, 0), (10, 10, self.hp/self.ratio_health_bar, 20))
        pygame.draw.rect(sv.surface, (255, 255, 255), (10, 10, 200, 20),4)

    # getters e setters
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__naem = name
    
    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, rect):
        self.__rect = rect
    
    @property
    def hitbox(self):
        return self.__hitbox
    
    @rect.setter
    def hitbox(self, hitbox):
        self.__hitbox = hitbox


