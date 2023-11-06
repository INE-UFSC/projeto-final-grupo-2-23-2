from abc import ABC

class Item(ABC):
    def __init__(self, name, category, description, rarity, usage_interval, image, dropped, x,y):
        self.__name = name
        self.__category = category
        self.__description = description
        self.__rarity = rarity
        self.__usage_interval = usage_interval
        self.__image = image
        self.__dropped = dropped
        self.__x = x
        self.__y = y
        
    @property
    def name(self):
        return self.__name
    
    @property
    def category(self):
        return self.__category
    
    @property
    def description(self):
        return self.__description
    
    @property
    def rarity(self):
        return self.__rarity
    
    @property
    def usage_interval(self):
        return self.__usage_interval
    
    @property
    def image(self):
        return self.__image
    
    @property
    def dropped(self):
        return self.__dropped
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.setter
    def set_x(self,x):
        self.__x = x
    
    @y.setter
    def set_y(self, y):
        self.__y = y