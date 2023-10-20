from data.components.Item import Item


class Inventario:
    def __init__(self):
        self.__tamanho = None
        self.__itens = None

    def adicionar_item(self, item):
        if isinstance(item, Item):
            self.__itens.append(item)
        else:
            pass

    def remover_item(self, item):
        if isinstance(item, Item):
            self.__itens.remove(item)
