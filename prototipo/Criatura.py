from Inventario import Inventario

class Criatura:
    def __init__(self, nome, classe, vida, velocidade, imagem, inventario, item_defensivo, item_ofensivo, morte,x,y):
        self.__nome = nome
        self.__classe = classe
        self.__vida = vida
        self.__velocidade = velocidade
        self.__imagem = imagem
        self.__inventario = inventario
        self.__item_ofensivo = item_ofensivo
        self.__item_defensivo = item_defensivo
        self.__morte = morte
        self.__x = x
        self.__y = y
    
    def mover(self):
        pass
    
    def atacar(self):
        pass
    
    def defender(self):
        pass
