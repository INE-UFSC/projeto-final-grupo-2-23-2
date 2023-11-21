from data.screens.screen import Screen
from data.screens.button import Button
import pygame

class IntroScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'intro'
        self.buttons = [Button((self.width/2 - 110), (self.height/2 - 100), 220, 50, (255,255,255), (0,0,0), 'Start Game', 32),
                        Button((self.width/2 - 150), (self.height/2), 300, 50, (255,255,255), (0,0,0), 'Configurations', 32),
                        Button((self.width/2 - 125), (self.height/2 + 100), 250, 50, (255,255,255), (0,0,0), 'Quit Game', 32)]
        

    def run(self):
        while self.primary:
            current_time = pygame.time.get_ticks()
            if current_time - self.wait_time >= self.game.last_click_time:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                
                button = self.get_button_clicks(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

                if button is not None:
                    self.game.last_click_time = current_time

                    if button.content == 'Start Game':
                        self.game.start()

                    if button.content == 'Configurations':
                        self.game.config_screen()

                    if button.content == 'Quit Game':
                        pygame.quit()

            self.blit()