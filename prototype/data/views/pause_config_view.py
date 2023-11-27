from data.views.view_menu import ViewMenu
from data.utils.button import Button
import pygame

class PauseConfigView(ViewMenu):
    def __init__(self):
        super().__init__()
        self.buttons = [
                Button((self.width/2 - 150), (self.height/2), 300, 50, (255,255,255), (0,0,0), 'Return to menu', 32),
                Button((self.width/2 - 150), (self.height/2 - 100), 300, 50, (255,255,255), (0,0,0), 'Return to game', 32)
            ]


    def render(self, game):
        while self.primary:
            current_time = pygame.time.get_ticks()
            if current_time - self.wait_time >= game.game_model.last_click_time:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.close()
                
                button = self.get_button_clicks(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

                if button is not None:
                    game.game_model.last_click_time = current_time
                    if button.content == 'Return to game':
                        game.game_model.start()
                    if button.content == 'Return to menu':
                        game.choose_view("pause")
            self.blit()