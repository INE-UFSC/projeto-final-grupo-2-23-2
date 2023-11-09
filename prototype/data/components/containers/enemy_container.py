class EnemyContainer:
    def __init__(self):
        self.__enemies = []
    
    @property
    def enemies(self):
        return self.__enemies
    
    #todo: tratamento
    def add_enemy(self, enemy):
        self.__enemies.append(enemy)