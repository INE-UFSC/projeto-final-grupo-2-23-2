import pygame
import os

# controller -> player
class Ui():
    def __init__(self, controller):
        self.controller = controller
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + '/../../../resources/graphics/font/asman.ttf', 18)     

    def show_health_bar(self):
        # bg rect
        bg_rect = pygame.Rect(13, 13, 300, 30) 
        pygame.draw.rect(self.display_surface, "#222222", bg_rect) 
        
        # insider rect
        ratio = self.controller.player.hp / self.controller.player.max_hp
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, "red", current_rect)
        pygame.draw.rect(self.display_surface, "#111111", bg_rect, 5)

    def show_inventory(self):
        inventory = self.controller.player.inventory

        # bg rect
        size = 80 
        width = size * inventory.size()
        bg_rect = pygame.Rect(13, self.display_surface.get_height() - size - 13, width, size)
        pygame.draw.rect(self.display_surface, "#222222", bg_rect)

        # item rect
        for i in range(inventory.size()):
            item_width, item_height = inventory.items[i].image.get_size()
            x_position = bg_rect.left + (size * i) + (size - item_width) // 2
            y_position = bg_rect.top + (size - item_height) // 2
            self.display_surface.blit(inventory.items[i].image, (x_position, y_position))
            pygame.draw.rect(self.display_surface, "#111111", bg_rect, 5)

    def display(self):
        self.show_health_bar()
        self.show_inventory()