import pygame
from data.base.model import Model
from data.game.level_container import LevelContainer

class GameModel(Model):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.levels_container = LevelContainer()
        self.player = self.levels_container.level.controller.player

    def update(self):
        self.levels_container.level.run()
        self.input_handler()
    
    def input_handler(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        controller = self.levels_container.level.controller
        player = self.levels_container.level.controller.player

        if player.action == 'normal':
            if keys[pygame.K_UP]:
                player.direction.y = -1   
            elif keys[pygame.K_DOWN]:
                player.direction.y = 1  
            else:
                player.direction.y = 0
            if keys[pygame.K_LEFT]:
                player.direction.x = -1
            elif keys[pygame.K_RIGHT]:
                player.direction.x = 1
            else:
                player.direction.x = 0
        
        if keys[pygame.K_SPACE]:
            player.create_attack(controller.visible_sprites, controller.attacks_sprites, current_time)
        
        if keys[pygame.K_LCTRL]:
            player.create_defense(controller.visible_sprites, controller.deffense_sprites, controller.obstacles_sprites, current_time)

        if keys[pygame.K_LSHIFT]:
            player.use_dash(current_time)

        if keys[pygame.K_c]:
            player.picking = True
        else:
            player.picking = False