import pygame
import os
import sys
from data.screens.screen_container import ScreenContainer
from data.elements.levels import Levels
from data.elements.levels import Level
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
        
        self.width, self.height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.intro_background = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + "/../resources/screens/intro2.png")
        self.view = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
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
        self.current_level = self.levels.get_level()
        
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
                        self.current_level = next_level


            if self.player == None:
                self.player = self.current_level.controller.player

            # morte
            if self.player.hp == 0:
                self.game_over()
                

            # prenchendo display com verde, reseta a malha
            self.current_level.surface.fill('#71ddee')

            # roda fase
            self.current_level.run()
            self.input_handler()

            # atualiza display
            pygame.display.flip()

            # define fps do jogo
            self.clock.tick(self.fps)

    def game_over(self):
        self.current_screen = self.screens.get_screen('game_over')
        self.current_screen.run()
        

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
        if not player.dashing:
            if keys[pygame.K_UP] and player.moving:
                player.direction.y = -1   
            elif keys[pygame.K_DOWN] and player.moving:
                player.direction.y = 1  
            else:
                player.direction.y = 0

            if keys[pygame.K_LEFT] and player.moving:
                player.direction.x = -1
            elif keys[pygame.K_RIGHT] and player.moving:
                player.direction.x = 1
            else:
                player.direction.x = 0
        
        # raid input
        if keys[pygame.K_SPACE]:
            if player.inventory.contains("raid") and (not player.attacking):
                try:
                    if current_time - player.inventory.get("raid").time >= player.inventory.get("raid").cooldown:
                        player.attacking = True
                        player.inventory.get("raid").time = pygame.time.get_ticks()
                        controller.create_attack()
                except:
                        player.attacking = True
                        player.inventory.get("raid").time = pygame.time.get_ticks()
                        controller.create_attack()
        
        # pick input
        if keys[pygame.K_c]:
            player.picking = True
        else:
            player.picking = False
        
        # guard input
        if keys[pygame.K_LCTRL]:
            if player.inventory.contains("guard"):
                try:
                    if current_time - player.inventory.get("guard").time >= player.inventory.get("guard").cooldown:
                        player.deffending = True
                        player.inventory.get("guard").time = pygame.time.get_ticks()
                        controller.create_defense()
                except:
                        player.deffending = True
                        player.inventory.get("guard").time = pygame.time.get_ticks()
                        controller.create_defense()


        # dash input 
        if keys[pygame.K_LSHIFT]:
            if player.inventory.contains("dash"):
                try:
                    if current_time - player.inventory.get("dash").time >= player.inventory.get("dash").cooldown:
                        player.use_dash()
                except:
                    player.use_dash()

        if keys[pygame.K_ESCAPE]:
            self.menu_screen()

