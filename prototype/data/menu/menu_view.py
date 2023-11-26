from data.base.view import View
from data.menu.button import Button
import pygame

class MenuView(View):
    def __init__(self):
        super().__init__()
        self.buttons = [
                Button((self.width/2 - 150), (self.height/2 - 100), 300, 50, (255,255,255), (0,0,0), 'Return to game', 32),
                Button((self.width/2 - 150), (self.height/2), 300, 50, (255,255,255), (0,0,0), 'Configurations', 32),
                Button((self.width/2 - 125), (self.height/2 + 100), 250, 50, (255,255,255), (0,0,0), 'Quit Game', 32)
            ]

    def render(self, game):
        while self.primary:
            current_time = pygame.time.get_ticks()
            if current_time - self.wait_time >= game.last_click_time:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.close()
                
                button = self.get_button_clicks(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

                if button is not None:
                    game.last_click_time = current_time

                    if button.content == 'Return to game':
                        game.start()
                        
                    if button.content == 'Configurations':
                        game.choose_view("config")

                    if button.content == 'Quit Game':
                        self.close()

            self.blit()

