from data.game.level import Level
from data.utils.exceptions.level_not_found import LevelNotFound

class LevelContainer:
    def __init__(self):
        self.__levels = [Level("level_1"),Level("level_2"), Level("level_3")]
        self.__level = None

    @property
    def level(self):
        if self.__level == None and len(self.levels) != 0:
            self.__level = self.levels[0]
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level


    @property
    def levels(self):
        return self.__levels

    def add_level(self, level:Level):
        if isinstance(level, Level):
            self.levels.append(level)

    def advance_level(self):
        index = self.levels.index(self.level) + 1
        if index != len(self.levels):
            self.level = self.levels[index]
        else:
            quit()
