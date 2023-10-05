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
        