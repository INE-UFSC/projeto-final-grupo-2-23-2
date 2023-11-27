from abc import ABC, abstractmethod
import pygame


class View(ABC):
    def __init__(self):
        self.__width = pygame.display.Info().current_w
        self.__height = pygame.display.Info().current_h
        self.__fullscreen = True
        self.__display = pygame.display.get_surface()

    @abstractmethod
    def render(self):
        pass

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def fullscreen(self):
        return self.__fullscreen

    @fullscreen.setter
    def fullscreen(self, fullscreen: bool):
        self.__fullscreen = fullscreen

    @property
    def display(self):
        return self.__display

    @display.setter
    def display(self, display):
        self.__display = display
