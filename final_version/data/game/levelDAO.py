from data.game.level import Level
from data.game.DAO import DAO 
from data.base.controller import Controller

class LevelDAO(DAO):
    def __init__(self, datasource = ''):
        super().__init__(datasource)

    def add(self, level: Level):
        if (level is not None) and (isinstance(level, level)) and (isinstance(level.controller, Controller)) and (isinstance(level.tilesize, int)):
            super().add(level.name, level.to_dict())
            
    def get(self, key):
        return super().get(key)
        
    def remove(self, key):
        return super().remove(key)
