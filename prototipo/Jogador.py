from Criatura import Criatura

class Jogador(Criatura):
    def __init__(self, nome, classe, vida, velocidade, imagem, inventario, item_defensivo, item_ofensivo, morte, x, y):
        super().__init__(nome, classe, vida, velocidade, imagem, inventario, item_defensivo, item_ofensivo, morte, x, y)
    
    def atacar():
        pass
    
    def defender():
        pass
    
    def pegar_item():
        pass