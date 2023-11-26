from data.screens.screen import Screen
from data.screens.button import Button
import pygame

class Config2Screen(Screen):
    def __init__(self):
        super().__init__()
        self.buttons = [
                Button((self.width/2 - 150), (self.height/2), 300, 50, (255,255,255), (0,0,0), 'Return to menu', 32),
            ]


    def run(self, game):
        while self.primary:
            current_time = pygame.time.get_ticks()
            if current_time - self.wait_time >= game.last_click_time:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.close()
                
                button = self.get_button_clicks(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

                if button is not None:
                    game.last_click_time = current_time
                    if button.content == 'Return to menu':
                        game.choose_screen("intro")

            self.blit()