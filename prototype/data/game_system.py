import pygame
import sys
from data.base.controller import Controller
from data.game.game_controller import GameController
from data.menu.menu_controller import MenuController
from data.utils.exceptions.view_not_found import ViewNotFound



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

    def show_menu(self, name):
        self.menu_controller.show_menu(name)
    
    def close(self):
        pygame.quit()
        sys.exit()

    def __initialize_pygame(self):
        pygame.init()

        width = pygame.display.Info().current_w
        height = pygame.display.Info().current_h
        pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        pygame.display.set_caption("PartsFinder")