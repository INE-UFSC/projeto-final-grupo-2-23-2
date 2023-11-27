from data.menu.menu_view import ViewMenu
from data.utils.button import Button


class IntroconfigView(ViewMenu):
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
                "game.show_menu('intro')"
            ),
        ]
