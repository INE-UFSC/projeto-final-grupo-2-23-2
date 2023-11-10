from data.components.items.item import Item
import pygame

class OffensiveItem(Item):
    def __init__(self, player, groups):
        super().__init__(player, groups)