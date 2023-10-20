from data.components.Fase import Fase


class ContainerFases:
    def __init__(self):
        self.__fases = [Fase("mvp")]
        self.__indice_fase_atual = 0

    @property
    def fases(self):
        return self.__fases

    @property
    def indice_fase_atual(self):
        return self.__indice_fase_atual

    # todo: adicionar_fase()

    # todo: tratar, os dois podem ser um so?
    def obter_fase(self):
        try:
            return self.fases[self.__indice_fase_atual]
        except:
            pass

    def obter_proxima_fase(self):
        self.__fase_indice_atual += 1
        self.obter_fase()
