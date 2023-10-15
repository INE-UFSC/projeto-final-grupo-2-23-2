import pygame, sys
from configuracoes import *
from Conteiners.Fase import Fase

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