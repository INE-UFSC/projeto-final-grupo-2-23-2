from data.game.creature import Creature
from data.utils.settings import Settings
from data.game.inventory import Inventory
from data.utils.support import import_folder
from data.utils.audio import Audio

from data.game.powerup import Powerup
from data.game.raid import Raid
from data.game.guard import Guard
from data.game.dash import Dash

import pygame
import os

class Player(Creature):
    def __init__(self):
        super().__init__("player", (0,0), [])
        self.sprite_type = 'player'
        self.import_assets()
        self.action = 'normal'
        self.inventory = Inventory()
        self.current_power = None
        self.picking = False

    def initialize(self, groups, position):
        self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + Settings().player_folder + self.name + '.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -26)
        self.generate(groups, position)

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

    def get_save_data(self):
        save_data = super().get_save_data()
        save_data['inventory'] = self.inventory.get_save_data()
        return save_data 
    
    def load_save_data(self, player_data):
        super().load_save_data(player_data)

        self.inventory.clear()
        inventory_data = player_data.get('inventory', {})
        items_data = inventory_data.get('items', [])
        

        for item_data in items_data:
            item_type = item_data.get('type', '')
            item_name = item_data.get('name', '')

            if item_type == 'powerup':
                if item_name == 'guard':
                    item_instance = Guard(item_name, self, [])
                    
                elif item_name == 'raid':
                    item_instance = Raid(item_name, self, [])
                    
                elif item_name == 'dash':
                    item_instance = Dash(item_name, self, [])

                self.inventory.add_item(item_instance)
        

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


    def create_attack(self, visible_sprites,attacks_sprites, current_time):
        if self.inventory.contains("raid") and (self.action == 'normal'):
            raid = self.inventory.get("raid")
            if current_time - raid.time >= raid.cooldown:
                self.action = 'attack'
                self.direction = pygame.math.Vector2()
                raid.time = pygame.time.get_ticks()
                self.current_power = Raid("raid", self,[visible_sprites,attacks_sprites])
                Audio().play_sound('raid')
                

    def create_defense(self, visible_sprites,deffense_sprites, obstacles_sprites, current_time):
        if self.inventory.contains("guard") and (self.action == 'normal'):
            guard = self.inventory.get("guard")

            if current_time - guard.time >= guard.cooldown:
                self.action = 'deffend'
                self.direction = pygame.math.Vector2()
                guard.time = pygame.time.get_ticks()
                self.current_power = Guard("guard",self,[visible_sprites,deffense_sprites, obstacles_sprites])
                Audio().play_sound('guard')
        
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
                Audio().play_sound('dash')

    def pick_item(self, item):
        if self.picking == True:
            if 'raid' == item.sprite_type:
                self.inventory.add_item(Raid(item.sprite_type, self,[]))
            if 'guard' == item.sprite_type:
                self.inventory.add_item(Guard(item.sprite_type, self,[]))
            if 'dash' == item.sprite_type: 
                self.inventory.add_item(Dash(item.sprite_type, self,[]))
            item.kill()