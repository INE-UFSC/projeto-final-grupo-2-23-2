import pygame
import os
import json

from data.utils.settings import Settings
from data.game.player import Player
from data.game.enemy import Enemy
from data.game.tile import Tile
from data.game.controller import Controller
from data.game.hud import Hud
from data.utils.support import import_csv_layout, import_folder
from random import choice

class Level:
    def __init__(self, map_name):
        self.name = map_name
        self.controller = Controller(self.name)
        self.tilesize = 64
        self.loaded = False

    def generate_map(self, player):
        cont = self.controller
        # loop pela matriz
        layout = {'boundary' : import_csv_layout(os.path.dirname(os.path.abspath(__file__))+ Settings().levels_folder + self.name + Settings().floor_blocks_csv),
                  'grass' : import_csv_layout(os.path.dirname(os.path.abspath(__file__))+ Settings().levels_folder + self.name + Settings().grass_csv),
                  'object' : import_csv_layout(os.path.dirname(os.path.abspath(__file__))+ Settings().levels_folder + self.name + Settings().map_objects_csv),
                  'entity' : import_csv_layout(os.path.dirname(os.path.abspath(__file__))+ Settings().levels_folder + self.name + Settings().map_entites_csv)
                  }
        
        graphics = {
             'grass' : import_folder(os.path.dirname(os.path.abspath(__file__))+ Settings().grass_texture_folder),
             'objects' : import_folder(os.path.dirname(os.path.abspath(__file__))+ Settings().objects_texture_folder)

        }
        for style, layout in layout.items():
            for lin_index, lin in enumerate(layout):
                for col_index, col in enumerate(lin):
                    x = (col_index ) * self.tilesize
                    y = (lin_index ) * self. tilesize
                    if col != '356' and col != '-1':
                        
                        if style == 'boundary':
                            Tile((x,y),[cont.obstacles_sprites],'invisible')
                        
                        if style == 'grass':
                                random_grass = choice(graphics['grass'])
                                Tile((x , y), [cont.visible_sprites],'grass', random_grass)
                        
                        if style == 'object':
                                objects = graphics['objects'][int(col)+13]
                                Tile((x, y), [cont.visible_sprites, cont.obstacles_sprites],'object', objects)

# <<<<<<< Save-Load
                        if self.loaded == False:
                            if style == 'entity':
                                if col == '391':
                                    Enemy("spirit", (x,y), [cont.visible_sprites,cont.attackable_sprites])
                                
                                if col == '393':
                                    Enemy("skeleton", (x,y), [cont.visible_sprites,cont.attackable_sprites])

                                if col == '392':
                                     Enemy("demon", (x,y), [cont.visible_sprites,cont.attackable_sprites])
                                    
                                if col == '394':
                                    player.initialize([cont.visible_sprites, cont.player_sprite], (x,y))    
                                    cont.player = player
                                    
                                if col == '532':
                                    Tile( (x,y), [cont.visible_sprites, cont.item_sprites], 'raid',
                                        pygame.image.load(os.path.dirname(os.path.abspath(__file__))+ Settings().raid_icon).convert_alpha())                            
                                
                                if col == '252':
                                    Tile( (x,y), [cont.visible_sprites, cont.item_sprites], 'guard',
                                        pygame.image.load(os.path.dirname(os.path.abspath(__file__))+ Settings().guard_icon).convert_alpha())

                                if col == '89':
                                    Tile( (x,y), [cont.visible_sprites, cont.item_sprites], 'dash',
                                        pygame.image.load(os.path.dirname(os.path.abspath(__file__))+ Settings().dash_icon).convert_alpha())
                                
        self._generated = True
        

    def run(self, player):
        if not hasattr(self, "_generated"):
            self.generate_map(player)
            self.ui = Hud(player)
        # desenha e atualiza o jogo
        self.controller.run()
        self.ui.display()

    def save(self, player):
        save_data = {
            'player': player.get_save_data(),
            'enemies': [enemy.get_save_data() for enemy in self.controller.attackable_sprites if isinstance(enemy, Enemy)],
        }

        save_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saves')
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        save_file_path = os.path.join(save_folder, f'{self.name}_save.json')
        with open(save_file_path, 'w') as save_file:
            json.dump(save_data, save_file)

    def load(self, level):
        save_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saves', f'level_{level}_save.json')

        if os.path.exists(save_file_path):
            with open(save_file_path, 'r') as save_file:
                save_data = json.load(save_file)

                player_data = save_data.get('player')
                if player_data:
                    player = Player()
                    position = player_data.get('position')
                    position = [int(coord) for coord in position]
                    player.initialize([self.controller.visible_sprites, self.controller.player_sprite], position)
                    player.load_save_data(player_data)
                    self.controller.player = player          

                enemies_data = save_data.get('enemies')
                if enemies_data:
                    for enemy_data in enemies_data:
                        enemy_name = enemy_data.get('name')
                        enemy_position = enemy_data.get('position')
                        enemy_position = [int(coord) for coord in enemy_position]

                        enemy_type = Settings.get_enemy_type(enemy_name)

                        enemy = Enemy(enemy_type, enemy_position, [])
                        enemy.initialize([self.controller.visible_sprites, self.controller.attackable_sprites], enemy_position)
                        enemy.load_save_data(enemy_data)
                        self.controller.attackable_sprites.add(enemy)
            
            
        self.loaded = True
        return player


    
