import os
import sys

# redefine o caminho de pesquisa
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data.Jogo import Jogo

# inicia o jogo
if __name__ == '__main__':
    jogo = Jogo()
    jogo.iniciar()
