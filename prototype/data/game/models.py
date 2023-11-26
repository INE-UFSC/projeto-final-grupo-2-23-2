from data.menu.intro_view import IntroView
from data.menu.menu_view import MenuView
from data.menu.config_view import ConfigView
from data.menu.config2_view import Config2View
from data.menu.gameover_view import GameoverView

# from prototype.data.utils.exceptions.model_not_found import *
import pygame


class Models:
    def __init__(self):
        self.models = []
    #     self.views = [
    #         IntroView(),
    #         MenuView(),
    #         ConfigView(),
    #         GameOverView(),
    #         Config2View(),
    #     ]
    #     self.screen = None

    #     self.__initialize_display()

    # def __initialize_display(self):
    #     self.width, self.height = (
    #         pygame.display.Info().current_w,
    #         pygame.display.Info().current_h,
    #     )

    #     pygame.display.set_caption("PartsFinder")
    #     pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)

    # def choose_screen(self, name):
    #     for screen in self.views:
    #         screen_name = screen.__class__.__name__.lower().replace("screen", "")

    #         if screen_name == name:
    #             self.screen = screen
    #             break
    #     else:
    #         raise ViewNotFound(name)

    # def run(self, game):
    #     try:
    #         self.screen.run(game)
    #     except Exception:
    #         raise ViewNotRunned(self.screen)
