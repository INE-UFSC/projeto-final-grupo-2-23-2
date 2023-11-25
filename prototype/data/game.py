import pygame
import os
import sys
from data.screens.screens import Screens
from data.elements.levels import Levels
from data.elements.levels import Level
from data.components.settings import Settings

class Game:
    def __init__(self):
        pygame.init()

        self.screens = Screens(self)
        self.screen = None

        self.player = None

        # atributos
        self.clock = pygame.time.Clock()

        self.intro_background = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + Settings().game_intro)
        self.levels = Levels()
        self.level = self.levels.get_level()

        self.last_click_time = 0

    def run(self):
        self.intro_screen()

    # comeca
    def start(self):
        if self.player != None:
            if self.player.hp == 0:
                self.reset_game()
        else:
            self.play()

    def reset_game(self):
        # Reiniciar os atributos necessários para reiniciar o jogo
        self.levels = Levels()
        self.level = self.levels.get_level()
        
        self.player = None

        # Iniciar o jogo novamente
        self.play()


    # loop do jogo
    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    while True:
                        pygame.quit()
                        sys.exit()
        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        next_level = Level(f"level_{len(self.levels.levels) + 1}", self.player)
                        self.levels.add_level(next_level)
                        self.level = next_level


            if self.player == None:
                self.player = self.level.controller.player

            # morte
            if self.player.hp == 0:
                self.game_over()
                

            # prenchendo display com verde, reseta a malha
            self.level.surface.fill('#71ddee')

            # roda fase
            self.level.run()
            self.input_handler()

            # atualiza display
            pygame.display.flip()

            # define fps do jogo
            self.clock.tick(Settings().fps)

    def game_over(self):
        self.screen = self.screens.get_screen('game_over')
        self.screen.run()
        

    def intro_screen(self):
        self.screen = self.screens.get_screen('intro')
        self.screen.run()

    def menu_screen(self):
        self.screen = self.screens.get_screen('menu')
        self.screen.run()

    def config_screen(self):
        self.screen = self.screens.get_screen('config')
        self.screen.run()

    def input_handler(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        controller = self.level.controller
        player = controller.player


        # movement input
        if player.action == 'normal':
            if keys[pygame.K_UP]:
                player.direction.y = -1   
                player.status = 'up'

            elif keys[pygame.K_DOWN]:
                player.direction.y = 1  
            else:
                player.direction.y = 0

            if keys[pygame.K_LEFT]:
                player.direction.x = -1
                player.status = 'left'

            elif keys[pygame.K_RIGHT]:
                player.direction.x = 1
            else:
                player.direction.x = 0
        
        # raid input
        if keys[pygame.K_SPACE]:
            player.create_attack(controller.visible_sprites, controller.attacks_sprites, current_time)
        
        # guard input
        if keys[pygame.K_LCTRL]:
            player.create_defense(controller.visible_sprites, controller.deffense_sprites, controller.obstacles_sprites, current_time)

        # dash input 
        if keys[pygame.K_LSHIFT]:
            player.use_dash(current_time)

        # pick input
        if keys[pygame.K_c]:
            player.picking = True
        else:
            player.picking = False

        if keys[pygame.K_p]:
            self.menu_screen()
