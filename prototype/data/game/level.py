import pygame
import json
import os

from data.components.settings import Settings
from data.game.player import Player
from data.game.enemy import Enemy
from data.components.tile import Tile
from data.game.controller import Controller
from data.components.hud import Hud
from data.components.support import import_csv_layout, import_folder
from random import choice

class Level:
    def __init__(self, map_name):
        self.name = map_name
        self.controller = Controller(self.name)
        
        self.surface = pygame.display.get_surface()        
        self.tilesize = 64

        self.song = None  # name_song
        self.dropped_items = None  # dropped_items

        self.generate_map()
        self.ui = Hud(self.controller.player)


    def generate_map(self):
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
                                surface = graphics['objects'][int(col)+13]
                                Tile((x, y), [cont.visible_sprites, cont.obstacles_sprites],'object', surface)

                        if style == 'entity':
                            if col == '391':
                                Enemy("spirit", (x,y), [cont.visible_sprites,cont.attackable_sprites])
                            
                            if col == '393':
                                Enemy("skeleton", (x,y), [cont.visible_sprites,cont.attackable_sprites])
                                  
                            if col == '394':
                                cont.player = Player("player", (x,y), [cont.visible_sprites, cont.player_sprite])
                                
                            if col == '532':
                                Tile( (x,y), [cont.visible_sprites, cont.item_sprites], 'raid',
                                      pygame.image.load(os.path.dirname(os.path.abspath(__file__))+ Settings().raid_icon).convert_alpha())                            
                            
                            if col == '252':
                                Tile( (x,y), [cont.visible_sprites, cont.item_sprites], 'guard',
                                      pygame.image.load(os.path.dirname(os.path.abspath(__file__))+ Settings().guard_icon).convert_alpha())

                            if col == '89':
                                Tile( (x,y), [cont.visible_sprites, cont.item_sprites], 'dash',
                                      pygame.image.load(os.path.dirname(os.path.abspath(__file__))+ Settings().dash_icon).convert_alpha())

        

    def run(self):
        # desenha e atualiza o jogo
        self.controller.run()
        self.ui.display()
