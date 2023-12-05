from data.base.controller import Controller
from data.game.game_model import GameModel
from data.game.game_view import GameView
from data.utils.settings import Settings
from data.utils.audio import Audio
from data.game.level import Level
import pygame


class GameController(Controller):
    def __init__(self, game_system):
        super().__init__()
        self.__game_view = GameView()
        self.__game_model = GameModel()
        self.__game_system = game_system

    @property
    def game_view(self):
        return self.__game_view

    @game_view.setter
    def game_view(self, value):
        self.__game_view = value

    @property
    def game_model(self):
        return self.__game_model

    @game_model.setter
    def game_model(self, value):
        self.__game_model = value

    @property
    def game_system(self):
        return self.__game_system

    @game_system.setter
    def game_system(self, value):
        self.__game_system = value

    def play(self):
        if self.game_model.player.hp == 0:
            self.reset()
        else:
            self.run()

    def reset(self):
        self.game_model = GameModel()
        self.run()

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_system.close()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_system.show_menu("pause")

            self.game_view.render()
            self.game_model.update()

            if self.game_model.player.hp == 0:
                Audio().play_sound("death")
                self.game_system.show_menu("gameover")

            self.game_model.next_level_logic()

            clock.tick(60)
