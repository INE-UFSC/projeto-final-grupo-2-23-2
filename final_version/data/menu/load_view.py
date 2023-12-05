from data.menu.menu_view import MenuView
from data.menu.button import Button


class LoadView(MenuView):
    def __init__(self):
        super().__init__()
        self.buttons = [
            Button(
                (self.width / 2 - 150),
                (self.height / 2 - 100),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Level 1",
                "game.load(1)"
            ),
            Button(
                (self.width / 2 - 150),
                (self.height / 2),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Level 2",
                "game.load(2)"
            ),
            Button(
                (self.width / 2 - 150),
                (self.height / 2 + 100),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Level 3",
                "game.load(3)"
            ),
            Button(
                (self.width / 2 - 150),
                (self.height / 2 + 200),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Retornar ao Menu",
                "game.show_menu('intro')"
            ),

        ]
