from Criatura import Criatura

class Jogador(Criatura):
    def __init__(self, nome, classe, vida, velocidade, imagem, inventario, item_defensivo, item_ofensivo, morte, x, y):
        super().__init__(nome, classe, vida, velocidade, imagem, inventario, item_defensivo, item_ofensivo, morte, x, y)
        
    def pegar_item(self,item):
        self.__inventario.adicionar_item(item)