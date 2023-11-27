import pygame
from data.base.controller import Controller
from data.views.view_manager import ViewManager
from data.game.game_model import GameModel
from data.utils.exceptions.view_not_found import ViewNotFound
from data.utils.exceptions.view_not_rendered import ViewNotRendered


class GameController(Controller):
    def __init__(self):
        pygame.init()

        self.view_container = ViewManager()
        self.game_model = GameModel(self)


    def run(self):
        self.choose_view("intro")

    def choose_view(self, name):
        try:
            self.view_container.view = name
            self.view_container.render_view(self)
        except ViewNotFound as exception:
            print(exception)
        except ViewNotRendered as exception:
            print(exception)


    
    