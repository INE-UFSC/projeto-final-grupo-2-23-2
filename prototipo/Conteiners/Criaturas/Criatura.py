# from Inventario.Inventario import Inventario
from abc import abstractclassmethod,ABC
class Criatura(ABC):
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
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def classe(self):
        return self.__classe
    
    @property
    def vida(self):
        return self.__vida
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def imagem(self):
        return self.__imagem
    
    @property
    def inventario(self):
        return self.__inventario
    
    @property
    def item_ofensivo(self):
        return self.__item_ofensivo
    
    @property
    def item_defensivo(self):
        return self.__item_defensivo
    
    @property
    def morte(self):
        return self.__morte
    
    @property
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    
    def mover(self,input):
        if input == 'up':
            self.__y += self.__velocidade
        elif input == 'down':
            self.__y -= self.__velocidade
        elif input == 'left':
            self.__x -= self.__velocidade
        elif input == 'right':
            self.__x += self.__velocidade
            
    def atacar(self):
        self.__item_ofensivo.atacar()
    
    def defender(self):
        self.__item_defensivo.defender()
