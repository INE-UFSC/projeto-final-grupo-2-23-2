from Item import Item
class ItemOfensivo(Item):
    def __init__(self, nome, classe, descricao, raridade, intervalo_uso, imagem, largado, x, y, dano, range_ataque):
        super().__init__(nome, classe, descricao, raridade, intervalo_uso, imagem, largado, x, y)
        self.__dano = dano
        self.__range_ataque = range_ataque
    
    def atacar():
        pass