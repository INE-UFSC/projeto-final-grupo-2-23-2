import pygame
import os

class Ui():
    def __init__(self, controller):
        # general
        self.controller = controller
        self.display_surface = pygame.display.get_surface()
        # path and font size
        self.font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__))+'/../../../resources/graphics/font/asman.ttf', 18)

        # bar setup
        self.ratio_health_bar = self.controller.player.hp / 200 # tamanho da barra


    def health_bar(self):
        pygame.draw.rect(self.controller.visible_sprites.surface, (255, 0, 0), (10, 10, self.controller.player.hp/self.ratio_health_bar, 20))
        pygame.draw.rect(self.controller.visible_sprites.surface, (255, 255, 255), (10, 10, 200, 20),4)

    def display(self):
        self.health_bar()