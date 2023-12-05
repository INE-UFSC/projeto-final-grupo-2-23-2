

import pygame
import os


class Hud():
    def __init__(self, player):
        self.player = player
        self.display_surface = pygame.display.get_surface()

    def show_profile(self):
        # show image
        image = pygame.image.load(f'{os.path.dirname(os.path.abspath(__file__))}/../../resources/elements/creatures/{self.player.name}/{self.player.name}.png')

        width = image.get_width() + 10
        height = image.get_height() + 10
        bordered_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        bordered_surface.blit(image, (5, 5))
        pygame.draw.rect(bordered_surface, "#111111", (0, 0, width, height), 5)

        self.display_surface.blit(bordered_surface, (13,13))

        # bg rect
        bg_rect = pygame.Rect(20 + width, 13, 300, 30) 
        pygame.draw.rect(self.display_surface, "#222222", bg_rect) 
        
        # insider rect
        ratio = self.player.hp / self.player.max_hp
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, "red", current_rect)
        pygame.draw.rect(self.display_surface, "#111111", bg_rect, 5)


    def show_inventory(self):
        inventory = self.player.inventory

        # bg rect
        size = 80 
        width = size * inventory.size()
        bg_rect = pygame.Rect(13, self.display_surface.get_height() - size - 13, width, size)
        pygame.draw.rect(self.display_surface, "#222222", bg_rect)

        # item rect
        for i in range(inventory.size()):
            item_width, item_height = inventory.items[i].icon.get_size()
            x_position = bg_rect.left + (size * i) + (size - item_width) // 2
            y_position = bg_rect.top + (size - item_height) // 2
            self.display_surface.blit(inventory.items[i].icon, (x_position, y_position))
            pygame.draw.rect(self.display_surface, "#111111", bg_rect, 5)

    def display(self):
        self.show_profile()
        self.show_inventory()