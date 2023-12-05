import sys
import pygame
import os
from data.utils.audio import Audio
from data.base.controller import Controller
from data.game.game_controller import GameController
from data.menu.menu_controller import MenuController


class GameSystem(Controller):
    def __init__(self):
        self.__initialize_pygame()

        self.game_controller = GameController(self)
        self.menu_controller = MenuController(self)

    def run(self):
        self.show_menu("intro")

    def play(self):
        self.game_controller.play()

    def reset(self):
        self.game_controller.reset()

    def save(self):
        self.game_controller.save()
        self.play()
    
    def load(self, level):
        print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'game', 'saves', f'level_{level}_save.json'))
        if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'game', 'saves', f'level_{level}_save.json')):
            self.game_controller.load(level)
            self.play()
        else:
            print("Selecione um load válido")

    def show_menu(self, name):
        self.menu_controller.show_menu(name)
        
    def change_volume(self, input1):
        audio = Audio()
        if input1 == 'mute':
            audio.volume = 0
        elif input1 == 'lower':
            audio.volume -= 0.1
        elif input1 == 'more':
            audio.volume += 0.1
            
    def close(self):
        pygame.quit()
        sys.exit()

    def __initialize_pygame(self):
        pygame.init()

        Audio().play_music("music")

        width = pygame.display.Info().current_w
        height = pygame.display.Info().current_h
        pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        pygame.display.set_caption("PartsFinder")