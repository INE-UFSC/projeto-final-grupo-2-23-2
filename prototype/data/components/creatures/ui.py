import pygame
import os

# controller -> player
class Ui():
    def __init__(self, controller):
        self.controller = controller
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__))+'/../../../resources/graphics/font/asman.ttf', 18)     

    def show_health_bar(self):
        # bg rect
        bg_rect = pygame.Rect(10, 10, 200, 20) 
        pygame.draw.rect(self.display_surface, "#222222", bg_rect) 
        
        # insider rect
        ratio = self.controller.player.hp / self.controller.player.max_hp
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, "red", current_rect)
        pygame.draw.rect(self.display_surface, "#111111", bg_rect, 4)

    def show_inventory(self):
        pass

    def display(self):
        self.show_health_bar()
        self.show_inventory()