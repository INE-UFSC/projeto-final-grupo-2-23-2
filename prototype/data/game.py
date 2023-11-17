import pygame
import sys
from data.components.containers.level_container import LevelContainer
from data.components.containers.controller import Controller
from data.views.view_container import ViewContainer



class Game:
    def __init__(self):
        # inciando pygame
        pygame.init()

        # atributos
        self.player = None #todo: tem que ficar aqui?
        self.difficulty = None
        self.views = ViewContainer()

        # vai pra na tela depois, todo: nao vimos mvcnho
        self.width = 1920
        self.heigth = 1080
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.view = pygame.display.set_mode((self.width, self.heigth))
        pygame.display.set_caption('PartsFinder')
        #

        # demais atributos
        self.levels = LevelContainer()
        self.current_level = self.levels.get_level()
    # comeca
    def start(self):
        self.play()

    # loop do jogo
    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        print('hey')
                        self.current_level = self.levels.get_next_level()
                        print(self.current_level)


            if self.player == None:
                self.player = self.current_level.controller.player

            # morte
            if self.player.hp == 0:
                pygame.quit()

            # prenchendo display com verde, reseta a malha
            self.current_level.surface.fill('black')

            # roda fase
            self.current_level.run()
            self.input_handler()

            # atualiza display
            pygame.display.update()

            # define fps do jogo
            self.clock.tick(self.fps)


    def menu_principal(self):
        pass

    def input_handler(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        controller = self.current_level.controller
        player = controller.player


        # movement input
        if not player.dashing:
            if keys[pygame.K_UP] and player.moving:
                player.direction.y = -1   
                player.status = 'up'

            elif keys[pygame.K_DOWN] and player.moving:
                player.direction.y = 1  
                player.status = 'down'
            else:
                player.direction.y = 0

            if keys[pygame.K_LEFT] and player.moving:
                player.direction.x = -1
                player.status = 'left'

            elif keys[pygame.K_RIGHT] and player.moving:
                player.direction.x = 1
                player.status = 'right'
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
            