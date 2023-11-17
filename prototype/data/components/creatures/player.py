from data.components.creatures.creature import Creature
from data.components.creatures.inventory import Inventory
from data.components.creatures.support import import_folder
import pygame
import os

class Player(Creature):
    def __init__(self, name, hp, position, groups, obstacle_sprites):
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

    def update(self):
        self.get_status()
        self.animate()
        self.move()
 
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        destroy_defense = False
        destroy_attack = False

        if self.attacking:
            self.moving = False
            if current_time - self.inventory.get("raid").time >= self.inventory.get("raid").cooldown:
                self.attacking = False
                self.moving = True
                destroy_attack = True
                self.status = self.status.split("_")[0]
        
        if self.invincible:
            if current_time - self.invincible_time >= self.invincible_cooldown:
                self.invincible = False

        if self.deffending:
            self.moving = False
            if current_time - self.inventory.get("guard").time >= self.inventory.get("guard").cooldown:
                self.deffending = False
                self.moving = True
                destroy_defense = True
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

        return destroy_attack, destroy_defense

    def use_dash(self):
        self.inventory.get("dash").get_player_direction()
        self.inventory.get("dash").time = pygame.time.get_ticks()
        self.dashing = True
        self.invincible = True
        self.invincible_time = pygame.time.get_ticks()