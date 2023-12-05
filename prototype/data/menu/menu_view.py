import pygame
import os
from data.utils.settings import Settings
from data.base.view import View
from abc import ABC


class MenuView(View, ABC):
    def __init__(self):
        super().__init__()

        # Atributos privados
        self.__background = pygame.image.load(
            os.path.dirname(os.path.abspath(__file__))
            + "/../../resources/screens/intro2.png"
        )
        self.__background_rect = self.__background.get_rect()

        self.__background_x = (self.width - self.__background_rect.width) // 2
        self.__background_y = (self.height - self.__background_rect.height) // 2

        self.__font = pygame.font.Font(
            os.path.dirname(os.path.abspath(__file__))
            + "/../../resources/fonts/stocky.ttf",
            32,
        )
        self.__title = self.__font.render("Parts Finder", True, (255, 255, 255))
        self.__title_rect = self.__title.get_rect(x=self.width / 2 - 130, y=10)

        self.__buttons = []
        self.__wait_time = 300
        self.__primary = True

    # Getters e setters
    @property
    def background(self):
        return self.__background

    @property
    def background_rect(self):
        return self.__background_rect

    @property
    def background_x(self):
        return self.__background_x

    @background_x.setter
    def background_x(self, value):
        self.__background_x = value

    @property
    def background_y(self):
        return self.__background_y

    @background_y.setter
    def background_y(self, value):
        self.__background_y = value

    @property
    def font(self):
        return self.__font

    @property
    def title(self):
        return self.__title

    @property
    def title_rect(self):
        return self.__title_rect

    @property
    def buttons(self):
        return self.__buttons

    @property
    def wait_time(self):
        return self.__wait_time

    @wait_time.setter
    def wait_time(self, value):
        self.__wait_time = value

    @property
    def primary(self):
        return self.__primary

    @primary.setter
    def primary(self, value):
        self.__primary = value

    def configure_screen(self):
        self.background_x = (self.width - self.__background_rect.width) // 2
        self.background_y = (self.height - self.__background_rect.height) // 2

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
