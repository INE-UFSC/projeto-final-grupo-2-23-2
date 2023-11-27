from data.views.intro_view import IntroView
from data.views.pause_view import PauseView
from data.views.pause_config_view import PauseConfigView
from data.views.intro_config_view import IntroConfigView
from data.views.gameover_view import GameoverView
from data.views.game_view import GameView
from data.views.view import View
from data.utils.exceptions.view_not_found import ViewNotFound
from data.utils.exceptions.view_not_rendered import ViewNotRendered
import pygame


class ViewManager:
    def __init__(self):    
        self.__view = None
        self.__views = [GameoverView(), GameView(), IntroConfigView(), IntroView(), PauseConfigView(), PauseView()]

        self.__width = pygame.display.Info().current_w
        self.__height = pygame.display.Info().current_h
        self.__fullscreen = True
        self.__display = None

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
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def fullscreen(self):
        return self.__fullscreen
    
    @fullscreen.setter
    def fullscreen(self, fullscreen: bool):
        self.__fullscreen = fullscreen

    @property
    def display(self):
        return self.__display

    @display.setter
    def display(self, display):
        self.__display = display

    def __initialize_display(self):        
        if self.__fullscreen:
            self.__display = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.__display = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("PartsFinder")