import pygame
import os

from data.components.settings import Settings
from data.elements.player import Player
from data.elements.enemy import Enemy
from data.components.tile import Tile
from data.elements.controller import Controller
from data.components.hud import Hud
from data.components.support import import_csv_layout, import_folder
from random import choice

class Level:
    def __init__(self, map_name, player = None):

        self.player = player
        self.name = map_name
        self.controller = Controller(self.name)
        
        self.surface = pygame.display.get_surface()        
        self.tilesize = 64

        self.song = None  # name_song
        self.dropped_items = None  # dropped_items

        self.generate_map()
        self.hud = Hud(self.controller.player)


    def generate_map(self):
        cont = self.controller
        # loop pela matriz
        
        layout = {'boundary' : import_csv_layout(os.path.dirname(os.path.abspath(__file__))+ Settings().levels_folder +self.name + Settings().floor_blocks_csv),
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
                                  self.controller.enemies = Enemy("skeleton", (x,y), [cont.visible_sprites,cont.attackable_sprites], cont.visible_sprites, cont.obstacles_sprites)
                                  
                            if col == '394':
                                if self.player:
                                    cont.update_player(Player("player", (x,y), [cont.visible_sprites, cont.player_sprite],cont.obstacles_sprites), self.player.inventory) 
                                else:
                                    cont.player = Player("player", (x,y), [cont.visible_sprites, cont.player_sprite],cont.obstacles_sprites)
                                
                            if col == '376':
                                Tile( (x + (3 * 64), y + (5 * 64)), [cont.visible_sprites, cont.item_sprites], 'raid', pygame.image.load(os.path.dirname(os.path.abspath(__file__))+ Settings().raid_icon).convert_alpha())                            
                            
                            if col == '252':
                                Tile( (x,y), [cont.visible_sprites, cont.item_sprites], 'guard', pygame.image.load(os.path.dirname(os.path.abspath(__file__))+ Settings().guard_icon).convert_alpha() )

                            if col == '89':
                                Tile( (x,y), [cont.visible_sprites, cont.item_sprites], 'dash', pygame.image.load(os.path.dirname(os.path.abspath(__file__))+ Settings().dash_icon).convert_alpha())

        

    def run(self):
        # desenha e atualiza o jogo
        self.controller.visible_sprites.custom_draw(self.controller.player)
        self.controller.player_cooldowns()
        self.controller.visible_sprites.update()
        self.controller.visible_sprites.enemy_update(self.controller.player)
        self.controller.player_attack_logic()
        self.controller.player_defense_logic()
        self.controller.player_collect_item()
        self.hud.display()
