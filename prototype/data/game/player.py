from data.game.creature import Creature
from data.components.settings import Settings
from data.game.inventory import Inventory
from data.components.support import import_folder

from data.game.raid import Raid
from data.game.guard import Guard
from data.game.dash import Dash

import pygame
import os

class Player(Creature):
    def __init__(self, name, position, groups):
        super().__init__(name, position, groups)
        
        self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + Settings().player_folder + self.name + '.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -26)
        self.sprite_type = 'player'
        self.import_assets()
        
        # movement
#         self.direction = pygame.math.Vector2()
#         self.moving = True
#         self.normal_speed = 5
#         self.speed = 4

        # action 
        self.action = 'normal'


        # items
        self.inventory = Inventory()

        # player stamina
        self.max_stamina = 200
        self.stamina = 200
        self.stamina_time = 0
        self.stamina_cooldown = 100
        
#         # player status
#         self.deffending = False
#         self.dashing = False
#         self.picking = False    

        #actions
        self.current_power = None
        self.picking = False

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not "_" in self.status:
                self.status = self.status + "_idle"
                
        if self.action != 'normal':
            if not self.action in self.status:
                splited_status = self.status.split("_")
                if len(splited_status) == 1:
                    self.status = self.status + f"_{self.action}"
                else:
                    splited_status[1] = self.action
                    self.status = "_".join(splited_status)

    def update(self, obstacle_sprites):
        self.get_status()
        self.animate()
        self.move(obstacle_sprites)
        self.cooldowns()
 
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.action == 'attack':
            raid = self.inventory.get("raid")
            if current_time - raid.time >= raid.duration:
                self.action = 'normal'
                self.destroy_power()
                self.status = self.status.split("_")[0]
        
        if self.invincible:
            if current_time - self.invincible_time >= self.invincible_cooldown:
                self.invincible = False

        if self.action == 'deffend':
            guard = self.inventory.get("guard")

            if current_time - guard.time >= guard.duration:
                self.action = 'normal'
                self.destroy_power()
                self.status = self.status.split("_")[0]

        if self.action == 'dash':
            dash = self.inventory.get("dash")
            self.speed = dash.speed
            self.direction = dash.direction
            
            if current_time - dash.time >= dash.duration:
                self.action = 'normal'
                self.invincible = False
                self.speed = self.normal_speed
            
                self.status = self.status.split("_")[0]
              
        if current_time - self.stamina_time >= self.stamina_cooldown:
            self.stamina_time = current_time
            self.update_stamina()
            # print(self.stamina)

    # def use_dash(self):
    #     if self.stamina_check(self.inventory.get('dash').stamina_cost):
            
    #         self.inventory.get("dash").get_player_direction()
    #         self.inventory.get("dash").time = pygame.time.get_ticks()
    #         self.dashing = True
    #         self.invincible = True
    #         self.invincible_time = pygame.time.get_ticks()
            
    def update_stamina(self):
        if 'move' in self.status or 'idle' in self.status:
            if self.stamina < self.max_stamina:
                self.stamina += 20
                if self.stamina > self.max_stamina:
                    self.stamina = self.max_stamina 

    def stamina_check(self, cost):
        if self.stamina >= cost:
            self.stamina -= cost
            return True
    def create_attack(self, visible_sprites,attacks_sprites, current_time):
        if self.inventory.contains("raid") and (self.action == 'normal'):
            raid = self.inventory.get("raid")
            if current_time - raid.time >= raid.cooldown:
                self.action = 'attack'
                self.direction = pygame.math.Vector2()
                raid.time = pygame.time.get_ticks()
                self.current_power = Raid("raid", self,[visible_sprites,attacks_sprites])

    def create_defense(self, visible_sprites,deffense_sprites, obstacles_sprites, current_time):
        if self.inventory.contains("guard") and (self.action == 'normal'):
            guard = self.inventory.get("guard")

            if current_time - guard.time >= guard.cooldown:
                self.action = 'deffend'
                self.direction = pygame.math.Vector2()
                guard.time = pygame.time.get_ticks()
                self.current_power = Guard("guard",self,[visible_sprites,deffense_sprites, obstacles_sprites])
        
    def destroy_power(self):
        if self.current_power != None:
            self.current_power.kill()
            self.current_power = None

    def use_dash(self, current_time):
        if self.inventory.contains("dash") and (self.action == 'normal'):
            dash = self.inventory.get("dash")

            if current_time - dash.time >= dash.cooldown:
                dash.get_player_direction()
                dash.time = pygame.time.get_ticks()
                self.action = 'dash'
                self.invincible = True
                self.invincible_time = pygame.time.get_ticks()

    def pick_item(self, item):
        if self.picking == True:
            if 'raid' == item.sprite_type:
                self.inventory.add_item(Raid(item.sprite_type, self,[]))
            if 'guard' == item.sprite_type:
                self.inventory.add_item(Guard(item.sprite_type, self,[]))
            if 'dash' == item.sprite_type: 
                self.inventory.add_item(Dash(item.sprite_type, self,[]))
            item.kill()