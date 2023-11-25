import pygame
import json
import os

from data.elements.player import Player
from data.elements.enemy import Enemy
from data.components.tile import Tile
from data.elements.controller import Controller
from data.components.hud import Ui
from data.components.support import import_csv_layout, import_folder
from random import choice

class Level:
    def __init__(self, map_name):
        self.name = map_name
        self.controller = Controller()
        
        self.surface = pygame.display.get_surface()        
        self.tilesize = 64

        self.song = None  # name_song
        self.dropped_items = None  # dropped_items

        self.generate_map()
        self.ui = Ui(self.controller)


    def generate_map(self):
        cont = self.controller
        # loop pela matriz
        layout = {'boundary' : import_csv_layout(os.path.dirname(os.path.abspath(__file__))+f'/../../resources/levels/{self.name}/csvs/map_FloorBlocks.csv'),
                  'grass' : import_csv_layout(os.path.dirname(os.path.abspath(__file__))+f'/../../resources/levels/{self.name}/csvs/map_Grass.csv'),
                  'object' : import_csv_layout(os.path.dirname(os.path.abspath(__file__))+f'/../../resources/levels/{self.name}/csvs/map_Objects.csv'),
                  'entity' : import_csv_layout(os.path.dirname(os.path.abspath(__file__))+ f'/../../resources/levels/{self.name}/csvs/map_Entities.csv')
                  }
        
        graphics = {
             'grass' : import_folder(os.path.dirname(os.path.abspath(__file__))+f'/../../resources/textures/grass'),
             'objects' : import_folder(os.path.dirname(os.path.abspath(__file__))+f'/../../resources/textures/objects')

        }
        for style, layout in layout.items():
            for lin_index, lin in enumerate(layout):
                for col_index, col in enumerate(lin):
                    x = (col_index + 9) * self.tilesize
                    y = (lin_index + 11) * self. tilesize
                    if col != '-1':
                        if style == 'boundary':
                            Tile((x - (3 * 64),y - (5 * 64)),[cont.obstacles_sprites],'invisible')
                        
                        if style == 'grass':
                                random_grass = choice(graphics['grass'])
                                Tile((x + (7 * 64), y), [cont.visible_sprites],'grass', random_grass)
                        
                        if style == 'object':
                                surface = graphics['objects'][int(col)+13]
                                Tile((x + (7 * 64), y), [cont.visible_sprites, cont.obstacles_sprites],'object', surface)

                        if style == 'entity':
                            if col == '393':
                                  self.controller.enemies = Enemy("enemy", 100, (x,y), [cont.visible_sprites,cont.attackable_sprites], cont.visible_sprites, cont.obstacles_sprites)
                                  
                            if col == '394':
                                cont.player = Player("player", 100, (x,y), [cont.visible_sprites, cont.player_sprite],cont.obstacles_sprites)
                                
                            if col == '376':
                                Tile( (x + (3 * 64), y + (5 * 64)), [cont.visible_sprites, cont.item_sprites], 'raid', pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'/../../resources/elements/powerups/raid/full.png').convert_alpha())                            
                            
                            if col == '252':
                                Tile( (x,y), [cont.visible_sprites, cont.item_sprites], 'guard')

                            if col == '89':
                                Tile( (x,y), [cont.visible_sprites, cont.item_sprites], 'dash')

        

    def run(self):
        # desenha e atualiza o jogo
        self.controller.run()
        self.ui.display()
