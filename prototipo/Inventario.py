from Item import Item
class Inventario:
    def __init__(self, tamanho, itens):
        self.__tamanho = tamanho
        self.__itens = itens
        
    def adicionar_item(self,item):
        if isinstance(item, Item):
            self.__itens.append(item)
        else:
            pass
    
    def remover_item(self,item):
        if isinstance(item, Item):
            self.__itens.remove(item)