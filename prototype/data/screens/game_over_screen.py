from data.screens.screen import Screen
from data.screens.button import Button
import pygame

class GameOverScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'game_over'
        self.title = self.font.render('Game Over', True, (255,255,255))
        self.title_rect = self.title.get_rect(x = self.width/2 - 130, y = 100)
        self.buttons = [Button((self.width/2 - 150), (self.height/2 - 100), 300, 50, (255,255,255), (0,0,0), 'Reiniciar', 32),
                        Button((self.width/2 - 150), (self.height/2), 300, 50, (255,255,255), (0,0,0), 'Voltar ao menu principal', 32),
                        Button((self.width/2 - 125), (self.height/2 + 100), 250, 50, (255,255,255), (0,0,0), 'Sair do jogo', 32)]


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

                    if button.content == 'Reiniciar':
                        self.game.reset_game()

                    if button.content == 'Voltar ao menu principal':
                        self.game.intro_screen()

                    if button.content == 'Sair do jogo':
                        pygame.quit()

            self.blit()

