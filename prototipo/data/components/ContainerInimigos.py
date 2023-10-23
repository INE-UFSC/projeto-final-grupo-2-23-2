class ContainerInimigos:
    def __init__(self):
        self.__inimigos = []
    
    @property
    def inimigos(self):
        return self.__inimigos
    
    #todo: tratamento
    def adicionar_inimigo(self, inimigo):
        self.__inimigos.append(inimigo)