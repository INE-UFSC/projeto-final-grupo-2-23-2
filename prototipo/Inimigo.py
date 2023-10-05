from Criatura import Criatura

class Inimigo(Criatura):
    def __init__(self, nome, classe, vida, velocidade, imagem, inventario, item_defensivo, item_ofensivo, morte, x, y):
        super().__init__(nome, classe, vida, velocidade, imagem, inventario, item_defensivo, item_ofensivo, morte, x, y)
        
    def atacar():
        pass
    
    def defender():
        pass