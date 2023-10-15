from Item import Item

class ItemDefensivo(Item):
    def __init__(self, nome, classe, descricao, raridade, intervalo_uso, imagem, largado, x, y, protecao):
        super().__init__(nome, classe, descricao, raridade, intervalo_uso, imagem, largado, x, y)
        self.__protecao = protecao
        
    def defender():
        pass
    
    @property
    def protecao(self):
        return self.__protecao