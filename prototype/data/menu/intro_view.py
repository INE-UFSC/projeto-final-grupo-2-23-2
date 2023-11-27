from data.menu.menu_view import MenuView
from data.menu.button import Button


class IntroView(MenuView):
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
