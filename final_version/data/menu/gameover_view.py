from data.menu.menu_view import MenuView
from data.menu.button import Button


class GameoverView(MenuView):
    def __init__(self):
        super().__init__()
        self.title = self.font.render("Game Over", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(x=self.width / 2 - 130, y=100)
        self.buttons = [
            Button(
                (self.width / 2 - 150),
                (self.height / 2 - 100),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Reiniciar",
                "game.reset()"
            ),
            Button(
                (self.width / 2 - 150),
                (self.height / 2),
                300,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Voltar ao menu principal",
                "game.show_menu('intro')"
            ),
            Button(
                (self.width / 2 - 125),
                (self.height / 2 + 100),
                250,
                50,
                (255, 255, 255),
                (0, 0, 0),
                "Sair do jogo",
                "game.close()"
            ),
        ]