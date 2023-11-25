import pygame
import os
import sys
from data.screens.screen_container import ScreenContainer
from data.elements.levels import Levels
from data.elements.controller import Controller
from data.components.button import Button



class Game:
    def __init__(self):
        # inciando pygame
        pygame.init()

        # atributos
        self.player = None #todo: tem que ficar aqui?
        self.difficulty = None
        self.font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + '/../resources/fonts/stocky.ttf', 32)

        # self.width = 1920
        # self.heigth = 1080
        self.width = 1080
        self.height = 720
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.intro_background = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + "/../resources/screens/intro2.png")
        self.view = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('PartsFinder')
        
        self.views = ScreenContainer(self)
        #

        # demais atributos
        self.levels = Levels()
        self.current_level = self.levels.get_level()
        
        # Screens
        self.screens = ScreenContainer(self)
        self.current_screen = None
        self.last_click_time = 0

        # Others
        self.player = None

    # comeca
    def start(self):
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
                        self.current_level = self.levels.get_next_level()


            if self.player == None:
                self.player = self.current_level.controller.player

            # morte
            if self.player.hp == 0:
                self.game_over()
                #pygame.quit()

            # prenchendo display com verde, reseta a malha
            self.current_level.surface.fill('black')

            # roda fase
            self.current_level.run()
            self.input_handler()

            # atualiza display
            pygame.display.flip()

            # define fps do jogo
            self.clock.tick(self.fps)

    def game_over(self):
        pass

    def intro_screen(self):
        self.current_screen = self.screens.get_screen('intro')
        self.current_screen.run()

    def menu_screen(self):
        self.current_screen = self.screens.get_screen('menu')
        self.current_screen.run()

    def config_screen(self):
        self.current_screen = self.screens.get_screen('config')
        self.current_screen.run()

    def input_handler(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        controller = self.current_level.controller
        player = controller.player


        # movement input
        if player.action == 'normal':
            if keys[pygame.K_UP]:
                player.direction.y = -1   
                player.status = 'up'

            elif keys[pygame.K_DOWN]:
                player.direction.y = 1  
                player.status = 'down'
            else:
                player.direction.y = 0

            if keys[pygame.K_LEFT]:
                player.direction.x = -1
                player.status = 'left'

            elif keys[pygame.K_RIGHT]:
                player.direction.x = 1
                player.status = 'right'
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

