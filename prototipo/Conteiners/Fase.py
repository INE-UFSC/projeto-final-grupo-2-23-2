import pygame
from configuracoes import *
from tile import Tile
from .Criaturas.Jogador import Jogador
class Fase:
    # def __init__(self, nome, volume_musica, ConteinerInimigos, mapa, inimigos_vivos, itens_jogados):
    #     self.__nome = nome
    #     self.__musica = volume_musica
    #     self.__conteinerInimigos = ConteinerInimigos
    #     self.__inimigos_vivos = inimigos_vivos
    #     self.__itens_jogados = itens_jogados

    def __init__(self):
        

        self.display_superficie = pygame.display.get_surface()

        self.sprites_visiveis = pygame.sprite.Group()
        self.inimigos_visiveis = pygame.sprite.Group()
        self.sprites_obstaculos = pygame.sprite.Group()

        self.mapear_fase()
        
    def mapear_fase(self):
        for lin_index, lin in enumerate(MAPA_MUNDO):
            for col_index, col in enumerate(lin):
                x = col_index * TILESIZE
                y = lin_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.sprites_visiveis, self.sprites_obstaculos],'a')
                elif col == 'e':
                    Tile((x,y),[self.sprites_visiveis, self.inimigos_visiveis],'e')
                elif col == 'p':
                    self.jogador = Jogador((x,y),[self.sprites_visiveis])
    
    def run(self):
        self.sprites_visiveis.draw(self.display_superficie)
        self.sprites_visiveis.update()
        self.inimigos_visiveis.update()
        

    
    # @property
    # def nome(self):
    #     return self.__nome
    
    # @property
    # def musica(self):
    #     return self.__musica
    
    # @property
    # def conteinerInimigos(self):
    #     return self.__conteinerInimigos
    
    # @property
    # def inimigos_vivos(self):
    #     return self.__inimigos_vivos
    
    # @property
    # def itens_jogados(self):
    #     return self.__itens_jogados
    