from data.menu.menu_view import MenuView
from data.menu.button import Button


class PauseView(MenuView):
    def __init__(self):
        super().__init__()
        self.__buttons = [
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
            Button(
                (self.width / 2 - 150),
                (self.height / 2),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Configurations",
                "game.show_menu('pauseconfig')"
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

    # Getters e setters
    @property
    def buttons(self):
        return self.__buttons

    @buttons.setter
    def buttons(self, new_buttons):
        if isinstance(new_buttons, list):
            self.__buttons = new_buttons
        else:
            raise ValueError("Buttons must be a list of Button objects.")
