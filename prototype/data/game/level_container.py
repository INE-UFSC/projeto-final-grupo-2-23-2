from data.game.level import Level
from data.utils.exceptions.level_not_found import LevelNotFound

class LevelContainer:
    def __init__(self):
        self.__levels = [Level("level_3")]
        self.__level = None

        self.index_current_level = 0

    def get_level(self):
        return self.levels[0]

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, name):
        for level in self.levels:
            if (level.name == name) and isinstance(level, Level):
                self.__level = level
                break
        else:
            raise LevelNotFound(name)

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
            self.level = self.levels[0]
