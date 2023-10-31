from data.components.item import Item


class Inventory:
    def __init__(self):
        self.__size = None
        self.__items = None

    def add_item(self, item):
        if isinstance(item, Item):
            self.__items.append(item)
        else:
            pass

    def remove_item(self, item):
        if isinstance(item, Item):
            self.__items.remove(item)
