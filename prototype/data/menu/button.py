from data.utils.settings import Settings
from data.utils.audio import Audio
import pygame
import os

class Button:
    def __init__(self, x, y, width, height, fg, bg, content, action):
        self.__font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + Settings().button_font, 32)
        self.__content = content
        self.__action = action

        self.__x = x
        self.__y = y
        self.__height = height
        self.__width = width

        self.__fg = fg
        self.__bg = bg

        self.__image = pygame.Surface((self.__width, self.__height))
        self.__image.fill(self.__bg)
        self.__rect = self.__image.get_rect()

        self.__rect.x = self.__x
        self.__rect.y = self.__y

        self.__text = self.__font.render(self.__content, True, self.__fg)
        self.__text_rect = self.__text.get_rect(center=(self.__width/2, self.__height/2))
        self.__image.blit(self.__text, self.__text_rect)

    def is_pressed(self, pos, pressed):
        if self.__rect.collidepoint(pos):
            if pressed[0]:
                Audio().play_sound("menu")
                return True
            return False
        return False

    # Getters
    @property
    def font(self):
        return self.__font

    @property
    def content(self):
        return self.__content

    @property
    def action(self):
        return self.__action

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def fg(self):
        return self.__fg

    @property
    def bg(self):
        return self.__bg

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    @property
    def text(self):
        return self.__text

    @property
    def text_rect(self):
        return self.__text_rect

    # Setters
    @content.setter
    def content(self, new_content):
        self.__content = new_content
        # Atualizar a representação visual do botão aqui se necessário

    @action.setter
    def action(self, new_action):
        self.__action = new_action

    @x.setter
    def x(self, new_x):
        self.__x = new_x
        self.__rect.x = self.__x

    @y.setter
    def y(self, new_y):
        self.__y = new_y
        self.__rect.y = self.__y

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @width.setter
    def width(self, new_width):
        self.__width = new_width
        self.__rect.width = self.__width

    @fg.setter
    def fg(self, new_fg):
        self.__fg = new_fg

    @bg.setter
    def bg(self, new_bg):
        self.__bg = new_bg
        self.__image.fill(self.__bg)
