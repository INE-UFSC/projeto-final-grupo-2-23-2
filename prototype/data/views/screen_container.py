from data.views.screens.intro_screen import IntroScreen
from data.views.screens.menu_screen import MenuScreen
from data.views.screens.config_screen import ConfigScreen

class ScreenContainer:
    def __init__(self, game):
        self.game = game
        self.screens = [IntroScreen(self.game),
                      MenuScreen(self.game),
                      ConfigScreen(self.game)]

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
