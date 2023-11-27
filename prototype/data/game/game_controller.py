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
        self.game_view = GameView()
        self.game_model = GameModel()
        self.game_system = game_system

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
                    if event.key == pygame.K_t:
                        self.game_model.levels_container.advance_level()
                    elif event.key == pygame.K_ESCAPE:
                        self.game_system.show_menu("pause")

            self.game_view.render()
            self.game_model.update()

            if self.game_model.player.hp == 0:
                Audio().play_sound("death")
                self.game_system.show_menu("gameover")            

            clock.tick(60) 