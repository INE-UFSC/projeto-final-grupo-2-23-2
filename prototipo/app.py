import os, sys
from data.Jogo import Jogo

# path padrao absoluto
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# instanciacao e inicio do controle
if __name__ == '__main__':
    jogo = Jogo()
    jogo.iniciar()
