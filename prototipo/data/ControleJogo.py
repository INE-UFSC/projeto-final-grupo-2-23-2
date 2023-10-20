import pygame
class ControleJogo:
    def __init__(self,jogador, dificuldade, partida, tela, container_fases,container_telas):
        self.__jogador = jogador
        self.__dificuldade = dificuldade
        self.__tela = tela
        self.__container_fases = container_fases
        self.__container_telas = container_telas
        
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
    
    def jogar(self):
        pass
    
    def mudar_menu(self):
        pass
    
    def checar_vitoria(self):
        pass
    
    def checar_ataque(self):
        pass