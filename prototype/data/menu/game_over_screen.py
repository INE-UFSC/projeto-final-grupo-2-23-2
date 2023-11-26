from data.menu.screen import Screen
from data.menu.button import Button
import pygame

class GameOverScreen(Screen):
    def __init__(self):
        super().__init__()
        self.title = self.font.render('Game Over', True, (255,255,255))
        self.title_rect = self.title.get_rect(x = self.width/2 - 130, y = 100)
        self.buttons = [Button((self.width/2 - 150), (self.height/2 - 100), 300, 50, (255,255,255), (0,0,0), 'Reiniciar', 32),
                        Button((self.width/2 - 150), (self.height/2), 300, 50, (255,255,255), (0,0,0), 'Voltar ao menu principal', 32),
                        Button((self.width/2 - 125), (self.height/2 + 100), 250, 50, (255,255,255), (0,0,0), 'Sair do jogo', 32)]


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

                    if button.content == 'Reiniciar':
                        game.reset()

                    if button.content == 'Voltar ao menu principal':
                        game.choose_screen("intro")

                    if button.content == 'Sair do jogo':
                        self.close()

            self.blit()

