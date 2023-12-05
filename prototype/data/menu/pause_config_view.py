from data.menu.menu_view import MenuView
from data.menu.button import Button


class PauseconfigView(MenuView):
    def __init__(self):
        super().__init__()
        self.buttons = [
            Button(
                (self.width / 2 - 150),
                (self.height / 2 + 350),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Return to menu",
                "game.show_menu('pause')"
            ),
            Button(
                (self.width / 2 - 150),
                (self.height / 2 + 250),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Return to game",
                "game.play()"
            ),
            Button(
                (self.width / 2 + 50),
                (self.height / 2),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Increase Volume",
                "game.change_volume('more')"
            ),
            Button(
                (self.width / 2 - 350),
                (self.height / 2),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Decrease Volume",
                "game.change_volume('lower')"
            ),
        ]
