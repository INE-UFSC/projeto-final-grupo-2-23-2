from data.menu.menu_view import MenuView
from data.menu.button import Button
import pygame
import os

class WinView(MenuView):
    def __init__(self):
        super().__init__()

        self.background = pygame.image.load(
            os.path.dirname(os.path.abspath(__file__))
            + "/../../resources/screens/win.png"
        )
        self.buttons = [
            Button(
                (self.width / 2 - 125),
                (self.height / 2 + 350),
                250,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Quit Game",
                "game.close()"
            ),

        ]
