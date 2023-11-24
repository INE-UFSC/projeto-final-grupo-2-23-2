import pygame
import os
import sys
from data.screens.screens import Screens
from data.elements.levels import Levels
from data.elements.levels import Level
from data.components.settings import Settings
from data.components.exceptions import *


class Game:
    def __init__(self):
        pygame.init()

        self.player = None
        self.screens = Screens(self)
        self.levels = Levels()
        self.level = self.levels.get_level()


        # atributos
        self.clock = pygame.time.Clock()

        self.last_click_time = 0

    def run(self):
        self.choose_screen("intro")

    def reset(self):
        # Reiniciar os atributos necessários para reiniciar o jogo
        self.levels = Levels()
        self.level = self.levels.get_level()
        
        self.player = None

        # Iniciar o jogo novamente
        self.start()


    # loop do jogo
    def start(self):
        def play():
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

                if self.player.hp == 0:
                    self.player = None
                    self.choose_screen("gameover")                

                self.level.surface.fill('#71ddee')

                # roda fase
                self.level.run()
                self.input_handler()

                # atualiza display
                pygame.display.flip()

                # define fps do jogo
                self.clock.tick(Settings().fps)

        if self.player == None:
            play()
        else:
            if self.player.hp == 0:
                self.reset()
            else:
                play()
        
    def choose_screen(self, name):
        try:
            self.screens.choose_screen(name)
            self.screens.run(self)
        except ScreenNotFound as exception:
            print(exception)
        except ScreenNotRunned as exception:
            print(exception)

    def input_handler(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        controller = self.level.controller
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
                
        # pick input
        if keys[pygame.K_c]:
            player.picking = True
        else:
            player.picking = False
        
        # raid input
        if keys[pygame.K_SPACE]:
            if player.inventory.contains("raid") and (not player.attacking):
                if current_time - player.inventory.get("raid").time >= player.inventory.get("raid").cooldown:
                    player.attacking = True
                    player.inventory.get("raid").time = pygame.time.get_ticks()
                    controller.create_attack()
        
        # guard input
        if keys[pygame.K_LCTRL]:
            if player.inventory.contains("guard"):
                if current_time - player.inventory.get("guard").time >= player.inventory.get("guard").cooldown:
                    player.deffending = True
                    player.inventory.get("guard").time = pygame.time.get_ticks()
                    controller.create_defense()


        # dash input 
        if keys[pygame.K_LSHIFT]:
            if player.inventory.contains("dash"):
                if current_time - player.inventory.get("dash").time >= player.inventory.get("dash").cooldown:
                    player.use_dash()

        if keys[pygame.K_ESCAPE]:
            self.choose_screen("menu")


