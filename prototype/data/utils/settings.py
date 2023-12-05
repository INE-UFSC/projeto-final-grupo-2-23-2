import pygame

class Settings:

    _instance = None

    def __init__(self):
        self.__difficulty = None
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.__game_intro = '/../resources/screens/intro2.png'
        self.__creatures_folder = '/../../resources/elements/creatures/'
        self.__player_folder = '/../../resources/elements/creatures/player/'
        
        self.__levels_folder = '/../../resources/levels/'        
        self.__grass_texture_folder = '/../../resources/levels/textures/grass'
        self.__objects_texture_folder = '/../../resources/levels/textures/objects'
        
        self.__icons_folder = '/../../resources/elements/powerups/icons/'

        self.__floor_blocks_csv = '/csvs/map_FloorBlocks.csv'
        self.__grass_csv = '/csvs/map_Grass.csv'
        self.__map_objects_csv = '/csvs/map_Objects.csv'
        self.__map_entites_csv = '/csvs/map_Entities.csv'
        
        self.__raid_icon = '/../../resources/elements/powerups/icons/raid.png'
        self.__guard_icon = '/../../resources/elements/powerups/icons/guard.png'
        self.__dash_icon = '/../../resources/elements/powerups/icons/dash.png'

        self.__button_font = '/../../resources/fonts/stocky.ttf'
        
        self.__player = {'health': 200,
                       'speed': 5,
                       'invincible_cooldown': 500}
        
        self.__skeleton = {'health': 100,
                         'detect_range': 300,
                         'attack_range': 50,
                         'speed': 3,
                         'attack_damage': 25,
                         'attack_cooldown': 400
                         }
        
        self.__demon =   {'health': 50,
                         'detect_range': 400,
                         'attack_range': 50,
                         'speed': 2,
                         'attack_damage': 45,
                         'attack_cooldown': 200
                         }
        
        self.__spirit =   {'health': 200,
                         'detect_range': 500,
                         'attack_range': 40,
                         'speed': 3,
                         'attack_damage': 30,
                         'attack_cooldown': 300
                         }
        
        self.__guard = {'duration': 500,
                      'cooldown': 600
                      }
        
        self.__raid = {'duration': 200,
                     'cooldown': 400,
                     'damage': 40
                     }
        
        self.__dash = {'duration': 200,
                     'cooldown': 400,
                     'speed' : 20
                     }
        
    @property
    def difficulty(self):
        return self.__difficulty
    
    @difficulty.setter
    def difficulty(self, value):
        self.__difficulty = value

    @property
    def game_intro(self):
        return self.__game_intro
    
    @game_intro.setter
    def game_intro(self, value):
        self.__game_intro = value

    @property
    def creatures_folder(self):
        return self.__creatures_folder
    
    @creatures_folder.setter
    def creatures_folder(self, value):
        self.__creatures_folder = value

    @property
    def player_folder(self):
        return self.__player_folder
    
    @player_folder.setter
    def player_folder(self, value):
        self.__player_folder = value

    @property
    def levels_folder(self):
        return self.__levels_folder
    
    @levels_folder.setter
    def levels_folder(self, value):
        self.__levels_folder = value

    @property
    def grass_texture_folder(self):
        return self.__grass_texture_folder
    
    @grass_texture_folder.setter
    def grass_texture_folder(self, value):
        self.__grass_texture_folder = value

    @property
    def objects_texture_folder(self):
        return self.__objects_texture_folder
    
    @objects_texture_folder.setter
    def objects_texture_folder(self, value):
        self.__objects_texture_folder = value

    @property
    def icons_folder(self):
        return self.__icons_folder
    
    @icons_folder.setter
    def icons_folder(self, value):
        self.__icons_folder = value

    @property
    def floor_blocks_csv(self):
        return self.__floor_blocks_csv
    
    @floor_blocks_csv.setter
    def floor_blocks_csv(self, value):
        self.__floor_blocks_csv = value

    @property
    def grass_csv(self):
        return self.__grass_csv
    
    @grass_csv.setter
    def grass_csv(self, value):
        self.__grass_csv = value

    @property
    def map_objects_csv(self):
        return self.__map_objects_csv
    
    @map_objects_csv.setter
    def map_objects_csv(self, value):
        self.__map_objects_csv = value

    @property
    def map_entites_csv(self):
        return self.__map_entites_csv
    
    @map_entites_csv.setter
    def map_entites_csv(self, value):
        self.__map_entites_csv = value

    @property
    def raid_icon(self):
        return self.__raid_icon
    
    @raid_icon.setter
    def raid_icon(self, value):
        self.__raid_icon = value

    @property
    def guard_icon(self):
        return self.__guard_icon
    
    @guard_icon.setter
    def guard_icon(self, value):
        self.__guard_icon = value

    @property
    def dash_icon(self):
        return self.__dash_icon
    
    @dash_icon.setter
    def dash_icon(self, value):
        self.__dash_icon = value

    @property
    def button_font(self):
        return self.__button_font
    
    @button_font.setter
    def button_font(self, value):
        self.__button_font = value

    @property
    def player(self):
        return self.__player
    
    @player.setter
    def player(self, value):
        self.__player = value

    @property
    def skeleton(self):
        return self.__skeleton
    
    @skeleton.setter
    def skeleton(self, value):
        self.__skeleton = value

    @property
    def demon(self):
        return self.__demon
    
    @demon.setter
    def demon(self, value):
        self.__demon = value

    @property
    def spirit(self):
        return self.__spirit
    
    @spirit.setter
    def spirit(self, value):
        self.__spirit = value

    @property
    def guard(self):
        return self.__guard
    
    @guard.setter
    def guard(self, value):
        self.__guard = value

    @property
    def raid(self):
        return self.__raid
    
    @raid.setter
    def raid(self, value):
        self.__raid = value

    @property
    def dash(self):
        return self.__dash
    
    @dash.setter
    def dash(self, value):
        self.__dash = value

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

