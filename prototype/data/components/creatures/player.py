from data.components.creatures.creature import Creature
from data.components.creatures.inventory import Inventory
import pygame
import os
from data.components.creatures.support import import_folder

class Player(Creature):
    def __init__(self, name, hp, position, groups, obstacle_sprites, generate_attack, destroy_attack, generate_defense, destroy_defense):
        super().__init__(name, hp, position, groups, obstacle_sprites)
        
        self.name = name
        self.image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__))+'/../../../resources/graphics/player/' + name + '.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -26)
        self.sprite_type = 'player'
        self.import_assets()
        
        # movement 
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()
        self.moving = True

        self.normal_speed = 5

        # items
        self.inventory = Inventory()

        # player actions
        self.deffending = False
        self.dashing = False
        self.picking = False
        
        # metodos vindos de fase
        self.generate_attack = generate_attack
        self.destroy_attack = destroy_attack
        self.generate_defense = generate_defense
        self.destroy_defense = destroy_defense

    
    def import_assets(self):
        path = os.path.dirname(os.path.abspath(__file__))+'/../../../resources/graphics/' + self.name 
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
        
        # raid input
        if keys[pygame.K_SPACE]:
            if self.inventory.contains("raid") and (not self.attacking):
                self.attacking = True
                self.inventory.get("raid").time = pygame.time.get_ticks()
                self.generate_attack()
        
        # pick input
        if keys[pygame.K_c]:
            self.picking = True
        else:
            self.picking = False
        
        # guard input
        if keys[pygame.K_LCTRL]:
            if self.inventory.contains("guard"):
                self.deffending = True
                self.inventory.get("guard").time = pygame.time.get_ticks()
                self.generate_defense()


        # dash input 
        if keys[pygame.K_LSHIFT]:
            if self.inventory.contains("dash"):
                try:
                    if current_time - self.inventory.get("dash").time >= self.inventory.get("dash").cooldown:
                        self.use_dash()
                except:
                    self.use_dash()
            
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move()
 
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            self.moving = False
            if current_time - self.inventory.get("raid").time >= self.inventory.get("raid").cooldown:
                self.attacking = False
                self.moving = True
                self.destroy_attack()
                self.status = self.status.split("_")[0]
        
        if self.invincible:
            if current_time - self.invincible_time >= self.invincible_cooldown:
                self.invincible = False

        if self.deffending:
            self.moving = False
            if current_time - self.inventory.get("guard").time >= self.inventory.get("guard").cooldown:
                self.deffending = False
                self.moving = True
                self.destroy_defense()
                self.status = self.status.split("_")[0]

        if self.dashing:
            dash = self.inventory.get("dash")
            self.speed = dash.speed
            self.direction = dash.direction
            
            if current_time - dash.time >= dash.duration:
                self.dashing = False
                self.invincible = False
                self.speed = self.normal_speed
            
                self.status = self.status.split("_")[0]

    def use_dash(self):
        self.inventory.get("dash").get_player_direction()
        self.inventory.get("dash").time = pygame.time.get_ticks()
        self.dashing = True
        self.invincible = True
        self.invincible_time = pygame.time.get_ticks()