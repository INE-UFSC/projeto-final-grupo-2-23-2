from data.views.view import View
import pygame


class GameView(View):
    def __init__(self):
        super().__init__()

    def render(self, game):
        game.game_model.start()