class Fase:
    def __init__(self, nome, volume_musica, ConteinerInimigos, mapa, inimigos_vivos, itens_jogados):
        self.__nome = nome
        self.__musica = volume_musica
        self.__conteinerInimigos = ConteinerInimigos
        self.__inimigos_vivos = inimigos_vivos
        self.__itens_jogados = itens_jogados
        
    def mapear_fase():
        pass
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def musica(self):
        return self.__musica
    
    @property
    def conteinerInimigos(self):
        return self.__conteinerInimigos
    
    @property
    def inimigos_vivos(self):
        return self.__inimigos_vivos
    
    @property
    def itens_jogados(self):
        return self.__itens_jogados
    