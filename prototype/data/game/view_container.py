from data.menu.intro_view import IntroView
from data.menu.menu_view import MenuView
from data.menu.config_view import ConfigView
from data.menu.config2_view import Config2View
from data.menu.gameover_view import GameoverView

from data.base.view import View
from data.utils.exceptions.view_not_found import ViewNotFound
from data.utils.exceptions.view_not_rendered import ViewNotRendered
import pygame


class ViewContainer:
    def __init__(self):
        self.__views = [IntroView(), MenuView(), ConfigView(), GameoverView(), Config2View()]
        self.__view = None

        self.__initialize_display()

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, name):
        for view in self.__views:
            view_name = view.__class__.__name__.lower().replace("view", "")
            if (view_name == name) and isinstance(view, View):
                self.__view = view
                break
        else:
            raise ViewNotFound(name)

    def render_view(self, game):
        try:
            self.view.render(game)
        except Exception:
            raise ViewNotRendered(self.view)
    

    def __initialize_display(self):
        self.width, self.height = (
            pygame.display.Info().current_w,
            pygame.display.Info().current_h,
        )

        pygame.display.set_caption("PartsFinder")
        pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
