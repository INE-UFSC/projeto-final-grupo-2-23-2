from abc import ABC

class Item(ABC):
    def __init__(self,nome, classe, descricao, raridade, intervalo_uso, imagem, largado, x,y):
        self.__nome = nome
        self.__classe = classe
        self.__descricao = descricao
        self.__raridade = raridade
        self.__intervalo_uso = intervalo_uso
        self.__imagem = imagem
        self.__largado = largado
        self.__x = x
        self.__y = y
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def classe(self):
        return self.__classe
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def raridade(self):
        return self.__raridade
    
    @property
    def intervalo_uso(self):
        return self.__intervalo_uso
    
    @property
    def imagem(self):
        return self.__imagem
    
    @property
    def largado(self):
        return self.__largado
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.setter
    def set_x(self,x):
        self.__x = x
    
    @y.setter
    def set_y(self, y):
        self.__y = y