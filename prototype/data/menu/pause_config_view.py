from data.menu.menu_view import MenuView
from data.menu.button import Button


class PauseconfigView(MenuView):
    def __init__(self):
        super().__init__()

        self.__buttons = [
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

    # Getter e setter
    @property
    def buttons(self):
        return self.__buttons

    @buttons.setter
    def buttons(self, new_buttons):
        if isinstance(new_buttons, list):
            self.__buttons = new_buttons
        else:
            raise ValueError("Buttons must be a list of Button objects.")

    # Métodos adicionais para manipular os botões
    def add_button(self, button):
        if isinstance(button, Button):
            self.__buttons.append(button)
        else:
            raise ValueError("Button must be an instance of the Button class.")

    def remove_button(self, button):
        if button in self.__buttons:
            self.__buttons.remove(button)
        else:
            raise ValueError("Button not found in the list of buttons.")
