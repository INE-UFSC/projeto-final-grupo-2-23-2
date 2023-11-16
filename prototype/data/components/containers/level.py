import pygame
import json
import os

from data.components.creatures.player import Player
from data.components.creatures.enemy import Enemy
from data.components.containers.tiles.tile import Tile
from data.components.containers.controller import Controller
from data.components.creatures.ui import Ui

class Level:
    # todo: name_fase != map_name?
    def __init__(self, map_name):
        self.name = map_name
        self.map = self.__extract_map(map_name)
        self.controller = Controller()
        
        # pega a surface(tela) que ja existe
        self.surface = pygame.display.get_surface()        
        # todo: melhor localizacao
        self.tilesize = 64

        self.song = None  # name_song
        self.dropped_items = None  # dropped_items

        self.generate_map()
        self.ui = Ui(self.controller)

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
                    self.controller.player = Player(
                        "player", 100, (x, y), [self.controller.visible_sprites, self.controller.player_sprite],self.controller.obstacles_sprites)
                elif col == 'e':
                    self.controller.enemies = Enemy(
                        "enemy", 100, (x, y), [self.controller.visible_sprites,self.controller.attackable_sprites], self.controller.visible_sprites, self.controller.obstacles_sprites)
                elif col == 'w':
                    Tile("weapon_item", (x, y), [
                         self.controller.visible_sprites, self.controller.item_sprites])
                elif col == 'd':
                    Tile("defensive_item", (x, y), [
                         self.controller.visible_sprites, self.controller.item_sprites])
                elif col == 's':
                    Tile("dash_item", (x, y), [
                         self.controller.visible_sprites, self.controller.item_sprites])
                    
    def run(self):
        # desenha e atualiza o jogo
        self.controller.visible_sprites.custom_draw(self.controller.player)
        self.controller.player_cooldowns()
        self.controller.visible_sprites.update()
        self.controller.visible_sprites.enemy_update(self.controller.player)
        self.controller.player_attack_logic()
        self.controller.player_collect_item()
        self.ui.display()
        
