import json 
from abc import ABC


class DAO(ABC):
    def __init__(self, datasource = ''):
        self.datasource = datasource
        self.objectCache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        json.dump(self.objectCache, open(self.datasource, 'w'))

    def __load(self):
        self.objectCache = json.load(open(self.datasource, 'r'))

    def add(self, key, obj):
        if key in self.objectCache:
            print("Error when saving")
        else:
            self.objectCache[key] = obj
            self.__dump()
            self.__load()

    def get(self, key):
        try:
            return self.objectCache[key]
        except KeyError:
            pass

    
    def remove(self, key):
        try:
            self.objectCache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.objectCache.values()