from data.screens.intro_screen import IntroScreen
from data.screens.menu_screen import MenuScreen
from data.screens.config_screen import ConfigScreen
from data.screens.game_over_screen import GameOverScreen
import pygame

class Screens:
    def __init__(self, game):
        self.game = game
        pygame.display.set_caption('PartsFinder')
        self.width, self.height = pygame.display.Info().current_w, pygame.display.Info().current_h
        pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        self.screens = [IntroScreen(self.game), MenuScreen(self.game), ConfigScreen(self.game),
                        GameOverScreen(self.game)]

    def add_screen(self, screen):
        self.screens.append(screen)
        
    def remove_screen(self, screen):
        self.screens.remove(screen)
    
    def contains(self, name):
        for screen in self.screens:
            if screen.name == name:
                return True
        else:
            return False
    
    def get_screen(self, name):
        for screen in self.screens:
            if screen.name == name:
                return screen
        return None

    def size(self):
        return len(self.screens)
