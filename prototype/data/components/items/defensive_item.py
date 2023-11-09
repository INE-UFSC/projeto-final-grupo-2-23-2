from item import Item

class DefensiveItem(Item):
    def __init__(self, name, category, description, rarity, usage_interval, image, dropped, x, y, protection):
        super().__init__(name, category, description, rarity, usage_interval, image, dropped, x, y)
        self.__protection = protection
        
    def deffend():
        pass
    
    @property
    def protection(self):
        return self.__protection