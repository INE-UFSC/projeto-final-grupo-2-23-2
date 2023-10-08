class ContainerFases:
    def __init__(self, fases):
        self.__fases = fases
        
    def get_fase(self,fase):
        return self.__fases[fase]