class Inventory:
    def __init__(self):
        self.size = 0
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        self.size += 1
        
    def remove_item(self, item):
        self.items.remove(item)
