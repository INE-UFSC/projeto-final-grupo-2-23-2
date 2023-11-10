import pygame
import json
import os
from data.components.creatures.player import Player
from data.components.creatures.enemy import Enemy
from data.components.containers.enemy_container import EnemyContainer
from data.components.items.weapon import Weapon
from data.components.containers.tile import Tile
from data.components.containers.controller import Controller

class Level:
    # todo: name_fase != map_name?
    def __init__(self, map_name):
        self.__name = map_name
        self.__map = self.__extract_map(map_name)
        self.controller = Controller()
        self.__player = None
        self.__enemies = EnemyContainer()
        

        # pega a surface(tela) que ja existe
        self.surface = pygame.display.get_surface()        
        # todo: melhor localizacao
        self.__tilesize = 64

        self.__song = None  # name_song
        self.__dropped_items = None  # dropped_items

        self.current_attack = None

        self.generate_map()

    # todo: tratamento de excessoes try
    def __extract_map(self, map_name):
        file_name = os.path.dirname(os.path.abspath(
            __file__)) + "/../../../resources/map_data/" + map_name + ".json"
        # Carregando o map a partir do file JSON
        with open(file_name, 'r') as file:
            return json.load(file)

    def generate_map(self):
        # loop pela matriz
        for lin_index, lin in enumerate(self.map):
            for col_index, col in enumerate(lin):
                x = col_index * self.tilesize
                y = lin_index * self. tilesize
                if col == 'x':
                    Tile("tree", (x, y), [
                         self.controller.visible_sprites, self.controller.obstacles_sprites])
                elif col == 'p':
                    self.player = Player(
                        "player", 100, (x, y), [self.controller.visible_sprites], self.controller.visible_sprites, self.controller.obstacles_sprites,self.create_attack,self.destroy_attack)
                elif col == 'i':
                    self.enemy = Enemy(
                        "enemy", 100, (x, y), [self.controller.visible_sprites,self.controller.attackable_sprites], self.controller.visible_sprites, self.controller.obstacles_sprites)

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.controller.visible_sprites,self.controller.attacks_sprites])
        
    def destroy_attack(self):
        if self.current_attack != None:
            self.current_attack.kill()
            self.current_attack = None

    def player_attack_logic(self):
        if self.controller.attacks_sprites:
            for sprites_ataque in self.controller.attacks_sprites:
                collision_sprites = pygame.sprite.spritecollide(sprites_ataque,self.controller.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                            if target_sprite.hp == 0:
                                target_sprite.kill()
                            else:
                                target_sprite.take_damage(self.player.damage)

        
    def run(self):
        # desenha e atualiza o jogo
        self.controller.visible_sprites.custom_draw(self.player)
        self.controller.visible_sprites.update()
        self.controller.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
    
    
    
        
    # getters e setters
    @property
    def name(self):
        return self.__name

    @property
    def map(self):
        return self.__map

    @map.setter
    def map(self, map):
        self.__map = map
    
    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        self.__player = player

    @property
    def song(self):
        return self.__song

    @property
    def enemies(self):
        return self.__enemies

    @property
    def dropped_items(self):
        return self.__dropped_items

    @property
    def tilesize(self):
        return self.__tilesize

    @property
    def surface(self):
        return self.__surface

    @surface.setter
    def surface(self, surface):
        self.__surface = surface

