from data.components.items.item import Item


class Inventory:
    def __init__(self):
        self.size = 0
        self.items = []
        
        self.weapon = None
        self.defense = None
        self.dash = None

    def add_item(self, item):
        self.items.append(item)
        self.size += 1
        
    def remove_item(self, item):
        self.items.remove(item)
