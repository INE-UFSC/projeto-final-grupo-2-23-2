class Inventory:
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
    
    def contains(self, name):
        for item in self.items:
            if item.name == name:
                return True
        else:
            return False
    
    def get(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def size(self):
        return len(self.items)
