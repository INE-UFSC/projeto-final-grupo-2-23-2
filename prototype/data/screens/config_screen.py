from data.screens.screen import Screen
from data.screens.button import Button
import pygame

class ConfigScreen(Screen):
    def __init__(self,game):
        super().__init__(game)
        self.name = 'config'
        self.buttons = [Button((self.width/2 - 150), (self.height/2), 300, 50, (255,255,255), (0,0,0), 'Return to menu', 32),
                        Button((self.width/2 - 150), (self.height/2 - 100), 300, 50, (255,255,255), (0,0,0), 'Return to game', 32)]


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
                    if button.content == 'Return to menu':
                        self.game.menu_screen()

                    if button.content == 'Return to game':
                        self.game.play()

            self.blit()