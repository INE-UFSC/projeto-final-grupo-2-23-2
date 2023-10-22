import pygame
import json
import os
from data.components.Jogador import Jogador
from data.components.Inimigo import Inimigo
from data.components.ContainerInimigos import ContainerInimigos
from data.components.Arma import Arma

class Fase:
    # todo: nome_fase != nome_mapa?
    def __init__(self, nome_mapa):
        self.__nome = nome_mapa
        self.__mapa = self.__extrair_mapa(nome_mapa)
        self.__jogador = None
        
        #ataques
        self.ataque_atual = None

        # pega a superficie(tela) que ja existe
        self.superficie = pygame.display.get_surface()

        # todos os sprites e sprites que colidem
        self.__sprites_visiveis = YSortCameraGroup()
        self.__sprites_obstaculos = pygame.sprite.Group()

        # todo: melhor localizacao
        self.__tilesize = 64

        self.__musica = None  # nome_musica
        self.__inimigos = ContainerInimigos()
        self.__itens_jogados = None  # itens_jogados

        self.criar_mapa()
        
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
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador

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
        nome_arquivo = os.path.dirname(os.path.abspath(
            __file__)) + "/../../resources/map_data/" + nome_mapa + ".json"
        print(nome_arquivo)
        # Carregando o mapa a partir do arquivo JSON
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)

    def criar_mapa(self):
        # loop pela matriz
        for lin_index, lin in enumerate(self.mapa):
            for col_index, col in enumerate(lin):
                x = col_index * self.tilesize
                y = lin_index * self. tilesize
                if col == 'x':
                    Bloco("tree", (x, y), [
                         self.sprites_visiveis, self.sprites_obstaculos])
                elif col == 'p':
                    self.jogador = Jogador(
                        "jogador", (x, y), [self.sprites_visiveis], self.sprites_obstaculos,self.criar_ataque,self.destruir_ataque)
                elif col == 'i':
                    self.inimigo = Inimigo(
                        "nuvem", (x, y), [self.sprites_visiveis], self.sprites_obstaculos)

    def criar_ataque(self):
        self.ataque_atual = Arma(self.jogador,[self.sprites_visiveis])
        
    def destruir_ataque(self):
        if self.ataque_atual:
            self.ataque_atual.kill()
        self.ataque_atual = None
    
    def rodar(self):
        # desenha e atualiza o jogo
        self.sprites_visiveis.custom_draw(self.jogador)
        self.sprites_visiveis.update()
        self.sprites_visiveis.inimigo_update(self.jogador)

# todo : tratamento
class Bloco(pygame.sprite.Sprite):
    def __init__(self, nome, posicao, grupos):
        super().__init__(grupos)
        self.image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__)) + '/../../resources/graphics/objects/' + nome + '.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=posicao)
        self.hitbox = self.rect.inflate(0, -20)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # inicializacao
        super().__init__()
        self.superficie = pygame.display.get_surface()
        self.metade_largura = self.superficie.get_size()[0] // 2
        self.metade_altura = self.superficie.get_size()[1] // 2
        # desvia o mapa em referencia a tela
        self.desvio = pygame.math.Vector2( )

    # praticamente um draw()
    def custom_draw(self, jogador):
        # calculando desvio
        self.desvio.x = jogador.rect.centerx - self.metade_largura
        self.desvio.y = jogador.rect.centery - self.metade_altura

        # desenhando
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            desvio_posicao = sprite.rect.topleft - self.desvio
            self.superficie.blit(sprite.image, desvio_posicao)
            
    def inimigo_update(self,player):
        sprites_inimigos = [sprite for sprite in self.sprites() if hasattr(sprite, 'nome') and sprite.nome == 'nuvem']
        for inimigo in sprites_inimigos:
            inimigo.inimigo_update(player)