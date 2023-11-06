from data.components.containers.level import Level


class LevelContainer:
    def __init__(self):
        self.__levels = [Level("mvp")]
        self.__index_current_level = 0

    @property
    def levels(self):
        return self.__levels

    @property
    def index_current_level(self):
        return self.__index_current_level
    
    # todo: remover fase?

    # todo: tratamento de excessa o caso nao exista
    def add_level(self, map_name):
        self.levels.append(Level(map_name))

    # todo: tratar, logica pra alternar entre as duas automaticamente
    def get_level(self):
        try:
            return self.levels[self.__index_current_level]
        except:
            pass

    def get_next_level(self):
        self.__index_current_level += 1
        self.get_level()
