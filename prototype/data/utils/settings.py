import pygame

class Settings:

    _instance = None

    def __init__(self):
        self.difficulty = None
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.game_intro = '/../resources/screens/intro2.png'
        self.creatures_folder = '/../../resources/elements/creatures/'
        self.player_folder = '/../../resources/elements/creatures/player/'
        
        self.levels_folder = '/../../resources/levels/'        
        self.grass_texture_folder = '/../../resources/levels/textures/grass'
        self.objects_texture_folder = '/../../resources/levels/textures/objects'
        
        self.icons_folder = '/../../resources/elements/powerups/icons/'

        self.floor_blocks_csv = '/csvs/map_FloorBlocks.csv'
        self.grass_csv = '/csvs/map_Grass.csv'
        self.map_objects_csv = '/csvs/map_Objects.csv'
        self.map_entites_csv = '/csvs/map_Entities.csv'
        
        self.raid_icon = '/../../resources/elements/powerups/icons/raid.png'
        self.guard_icon = '/../../resources/elements/powerups/icons/guard.png'
        self.dash_icon = '/../../resources/elements/powerups/icons/dash.png'

        self.button_font = '/../../resources/fonts/stocky.ttf'
        
        self.player = {'health': 200,
                       'speed': 5,
                       'invincible_cooldown': 500}
        
        self.skeleton = {'health': 100,
                         'detect_range': 300,
                         'attack_range': 50,
                         'speed': 3,
                         'attack_damage': 25,
                         'attack_cooldown': 400
                         }
        
        self.demon =   {'health': 50,
                         'detect_range': 400,
                         'attack_range': 50,
                         'speed': 2,
                         'attack_damage': 45,
                         'attack_cooldown': 200
                         }
        
        self.spirit =   {'health': 200,
                         'detect_range': 500,
                         'attack_range': 40,
                         'speed': 3,
                         'attack_damage': 30,
                         'attack_cooldown': 300
                         }
        
        self.guard = {'duration': 500,
                      'cooldown': 600
                      }
        
        self.raid = {'duration': 200,
                     'cooldown': 400,
                     'damage': 40
                     }
        
        self.dash = {'duration': 200,
                     'cooldown': 400,
                     'speed' : 20
                     }
        
        
        

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def get_enemy_type(enemy_name):
        enemy_type_mapping = {
            "skeleton": "skeleton",
            "spirit": "spirit",
            "demon": "demon",
        }
        return enemy_type_mapping.get(enemy_name, enemy_name)