import pygame
import sys
import os

# adição de caminhos para facilitar a navegação nos diretórios
caminho_atual = os.path.abspath(os.path.dirname(__file__))
sys.path.append(caminho_atual+"/data")
sys.path.append(caminho_atual+"/data/components")
sys.path.append(caminho_atual+"/resources")

from map_data.mvp_map import *
from data.components.Fase import Fase

class Jogo:

    def __init__(self):

        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('PartsFinder')
        self.clock = pygame.time.Clock()
        self.fase = Fase()
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.tela.fill('black')
            self.fase.run() 
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()  