import pygame
import os
from data.utils.settings import Settings
from data.base.view import View
from abc import ABC


class MenuView(View, ABC):
    def __init__(self):
        super().__init__()

        self.background = pygame.image.load(
            os.path.dirname(os.path.abspath(__file__))
            + "/../../resources/screens/intro2.png"
        )
        self.background_rect = self.background.get_rect()

        self.background_x = (self.width - self.background_rect.width) // 2
        self.background_y = (self.height - self.background_rect.height) // 2

        self.font = pygame.font.Font(
            os.path.dirname(os.path.abspath(__file__))
            + "/../../resources/fonts/stocky.ttf",
            32,
        )
        self.title = self.font.render("Parts Finder", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(x=self.width / 2 - 130, y=10)

        self.buttons = []
        self.wait_time = 300
        self.primary = True

    def configure_screen(self):
        self.background_x = (self.width - self.background_rect.width) // 2
        self.background_y = (self.height - self.background_rect.height) // 2

    def draw_elements(self):
        self.display = pygame.display.get_surface()

        self.display.blit(self.background, (self.background_x, self.background_y))
        self.display.blit(self.title, self.title_rect)

        for button in self.buttons:
            self.display.blit(button.image, button.rect)

        pygame.display.flip()
        Settings().clock.tick(Settings().fps)

    def get_button_clicks(self, mouse_pos, mouse_pressed):
        for button in self.buttons:
            if button.is_pressed(mouse_pos, mouse_pressed):
                return button
        return None

    def render(self):
        self.configure_screen()
        self.draw_elements()
