import pygame
from data.game.level import Level
from data.base.model import Model
from data.game.level_container import LevelContainer
from data.components.settings import Settings

class GameModel(Model):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.last_click_time = 0
        self.levels_container = LevelContainer()
        self.player = None

    def reset(self):
        self.player = None
        self.level_container = LevelContainer()

    def update(self):
        pass