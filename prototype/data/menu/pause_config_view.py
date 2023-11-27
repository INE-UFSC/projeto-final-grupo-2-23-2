from data.menu.menu_view import MenuView
from data.utils.button import Button
import pygame


class PauseconfigView(MenuView):
    def __init__(self):
        super().__init__()
        self.buttons = [
            Button(
                (self.width / 2 - 150),
                (self.height / 2),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Return to menu",
                "game.show_menu('pause')"
            ),
            Button(
                (self.width / 2 - 150),
                (self.height / 2 - 100),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Return to game",
                "game.play()"
            ),
        ]
