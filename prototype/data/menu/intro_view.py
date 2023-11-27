from data.menu.menu_view import ViewMenu
from data.utils.button import Button


class IntroView(ViewMenu):
    def __init__(self):
        super().__init__()
        self.buttons = [
            Button(
                (self.width / 2 - 110),
                (self.height / 2 - 100),
                220,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Start Game",
                "game.play()"
            ),
            Button(
                (self.width / 2 - 150),
                (self.height / 2),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Configurations",
                "game.show_menu('introconfig')"
            ),
            Button(
                (self.width / 2 - 125),
                (self.height / 2 + 100),
                250,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Quit Game",
                "game.close()"
            ),
        ]
