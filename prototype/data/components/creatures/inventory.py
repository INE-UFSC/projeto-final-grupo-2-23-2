class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
    
    def contains(self, name):
        for item in self.items:
            if item == name:
                return True
        else:
            return False
