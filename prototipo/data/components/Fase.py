import pygame
import json
import os
from data.components.Jogador import *
from data.components.ContainerInimigos import ContainerInimigos


class Fase:
    # todo: nome_fase != nome_mapa?
    def __init__(self, nome_mapa):
        self.__nome = nome_mapa
        self.__mapa = self.__extrair_mapa(nome_mapa)
        self.__musica = None # nome_musica
        self.__inimigos = ContainerInimigos()
        self.__itens_jogados = None #itens_jogados

        # pygame interface
        self.__superficie = None
        self.__sprites_visiveis = None
        self.__sprites_obstaculos = None
        self.__tilesize = 64

    # getters e setters
    @property
    def nome(self):
        return self.__nome

    @property
    def mapa(self):
        return self.__mapa

    @mapa.setter
    def mapa(self, mapa):
        self.__mapa = mapa

    @property
    def musica(self):
        return self.__musica

    @property
    def inimigos(self):
        return self.__inimigos

    @property
    def itens_jogados(self):
        return self.__itens_jogados

    @property
    def tilesize(self):
        return self.__tilesize

    @property
    def superficie(self):
        return self.__superficie

    @superficie.setter
    def superficie(self, superficie):
        self.__superficie = superficie

    @property
    def sprites_visiveis(self):
        return self.__sprites_visiveis

    @sprites_visiveis.setter
    def sprites_visiveis(self, sprites_visiveis):
        self.__sprites_visiveis = sprites_visiveis

    @property
    def sprites_obstaculos(self):
        return self.__sprites_obstaculos

    @sprites_obstaculos.setter
    def sprites_obstaculos(self, sprites_obstaculos):
        self.__sprites_obstaculos = sprites_obstaculos

    # todo: tratamento de excessoes try
    def __extrair_mapa(self, nome_mapa):
        nome_arquivo = os.path.dirname(os.path.abspath(__file__)) + "/../../resources/map_data/" + nome_mapa + ".json"
        print(nome_arquivo)
        # Carregando o mapa a partir do arquivo JSON
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)

    def mapear(self):
        # gera superficie
        self.superficie = pygame.display.get_surface()
        self.sprites_visiveis = pygame.sprite.Group()
        # grupos dos sprites que colidem
        self.sprites_obstaculos = pygame.sprite.Group()

        for lin_index, lin in enumerate(self.mapa):
            for col_index, col in enumerate(lin):
                x = col_index * self.tilesize
                y = lin_index * self. tilesize
                if col == 'x':
                    Tile("tree", (x, y), [self.sprites_visiveis,
                         self.sprites_obstaculos])
                if col == 'p':
                    self.jogador = Jogador("nuvem", (x, y), [self.sprites_visiveis])

    def run(self):
        self.sprites_visiveis.draw(self.superficie)
        self.sprites_visiveis.update()

# todo : tratamento
class Tile(pygame.sprite.Sprite):
    def __init__(self, nome, pos, grupos):
        super().__init__(grupos)
        self.nome = nome
        self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + '/../../resources/graphics/objects/' + nome + '.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
