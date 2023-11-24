from data.screens.intro_screen import IntroScreen
from data.screens.menu_screen import MenuScreen
from data.screens.config_screen import ConfigScreen
from data.screens.game_over_screen import GameOverScreen
from data.components.exceptions import *
import pygame


class Screens:
    def __init__(self, game):
        self.screens = [IntroScreen(), MenuScreen(), ConfigScreen(), GameOverScreen()]
        self.screen = None

        self.__initialize_display()

    def __initialize_display(self):
        self.width, self.height = (
            pygame.display.Info().current_w,
            pygame.display.Info().current_h,
        )

        pygame.display.set_caption("PartsFinder")
        pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)

    def choose_screen(self, name):
        for screen in self.screens:
            screen_name = screen.__class__.__name__.lower().replace("screen", "")

            if screen_name == name:
                self.screen = screen
                break
        else:
            raise ScreenNotFound(name)

    def run(self, game):
        try:
            self.screen.run(game)
        except AttributeError:
            raise ScreenNotRunned(self.screen)
