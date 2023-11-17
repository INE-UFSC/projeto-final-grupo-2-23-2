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
        self.playerr = None #todo: tem que ficar aqui?
        self.difficulty = None
        self.views = ViewContainer()

        # vai pra na tela depois, todo: nao vimos mvcnho
        self.width = 1280
        self.heigth = 768
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

            # morte
            if self.current_level.controller.player.hp == 0:
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
        
        # attack input
        if keys[pygame.K_SPACE]:
            weapon = player.inventory.weapon
            if (weapon is not None) and (not player.attacking):
                try:
                    if current_time - weapon.time >= weapon.cooldown:
                        player.attacking = True
                        weapon.time = pygame.time.get_ticks()
                        controller.create_attack()
                except:
                    player.attacking = True
                    weapon.time = pygame.time.get_ticks()
                    controller.create_attack()
        
        # pick input
        if keys[pygame.K_c]:
            player.picking = True
        else:
            player.picking = False
        
        # deffend input
        if keys[pygame.K_LCTRL]:
            defense = player.inventory.defense
            if defense is not None:
                player.deffending = True
                defense.time = pygame.time.get_ticks()
                controller.create_defense()


        # dash input 
        if keys[pygame.K_LSHIFT]:
            dash = player.inventory.dash
            if dash is not None:
                try:
                    if current_time - dash.time >= dash.cooldown:
                        player.use_dash()
                except:
                    player.use_dash()
        