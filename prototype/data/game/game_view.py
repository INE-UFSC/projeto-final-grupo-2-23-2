from data.base.view import View
import pygame


class GameView(View):
    def __init__(self):
        super().__init__()

    def render(self):
        pygame.display.flip()
        self.display.fill("#71ddee")