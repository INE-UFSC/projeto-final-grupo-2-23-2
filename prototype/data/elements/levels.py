from data.elements.level import Level


class Levels:
    def __init__(self):
        self.levels = [Level("level_1"), Level("level_2")]
        self.index_current_level = 0


    # todo: tratamento de excessa o caso nao exista
    def add_level(self, map_name):
        self.levels.append(Level(map_name))

    # todo: tratar, logica pra alternar entre as duas automaticamente
    def get_level(self):
        try:
            return self.levels[self.index_current_level]
        except:
            pass

    def get_next_level(self):
        self.index_current_level += 1
        return self.get_level()
