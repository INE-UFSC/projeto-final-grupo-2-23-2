import pygame
import sys
from data.components.Jogador import Jogador
from data.components.ContainerFases import ContainerFases
from data.components.Fase import Fase
# from data.components.ContainerTelas import ContainerTelas


class Jogo:
    def __init__(self):
        self.__jogador = None
        self.__dificuldade = None
        self.tela = None
        self.__fases = ContainerFases()
        # self.__telas = ContainerTelas()

        # pygame todo: nsei mvc
        self.__largura = 1280
        self.__altura = 720
        self.__fps = 60


    # getters e setters
    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self.__dificuldade = dificuldade

    @property
    def fases(self):
        return self.__fases

    @property
    def telas(self):
        return self.__telas

    def controlador(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.__jogador.mover('up')
        elif keys[pygame.K_DOWN]:
            self.__jogador.mover('down')

        if keys[pygame.K_RIGHT]:
            self.__jogador.mover('right')
        elif keys[pygame.K_LEFT]:
            self.__jogador.mover('left')

    def iniciar(self):
        self.jogar()

    def jogar(self):
        pygame.init()
        self.tela = pygame.display.set_mode((self.__largura, self.__altura))
        pygame.display.set_caption('PartsFinder')
        self.clock = pygame.time.Clock()
        self.fase = self.fases.obter_fase()
        self.fase.mapear()


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.tela.fill('black')
            self.fase.run()
            pygame.display.update()
            self.clock.tick(self.__fps)

    def mudar_menu(self):
        pass

    def checar_vitoria(self):
        pass

    def checar_ataque(self):
        pass
