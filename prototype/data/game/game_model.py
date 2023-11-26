from data.base.model import Model
from data.game.level_container import LevelContainer

class GameModel(Model):
    def __init__(self):
        self.__level_container = LevelContainer()
        self.__player = None
    
    @property
    def level_container(self):
        return self.__level_container
    
    @property
    def player(self):
        return self.__player
    
    @player.setter
    def player(self, player):
        self.__player = player
    
    def update(self):
        pass
