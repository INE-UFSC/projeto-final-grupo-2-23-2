import pygame
from data.base.controller import Controller
import os
import sys
from data.game.models import Models
from data.game.view_container import ViewContainer
from data.game.game_model import GameModel
from data.game.level import Level

from data.components.settings import Settings
from data.utils.exceptions.view_not_found import ViewNotFound
from data.utils.exceptions.view_not_rendered import ViewNotRendered


class GameController(Controller):
    def __init__(self):
        self.__models = Models()
        self.__view_container = ViewContainer()
        self.game_model = GameModel()

        pygame.init()

        # atributos
        self.clock = pygame.time.Clock()

        self.last_click_time = 0

    @property
    def view_container(self):
        return self.__view_container

    def run(self):
        self.choose_view("intro")

    def reset(self):
        # Reiniciar os atributos necessários para reiniciar o jogo
        # self.game_model.levels = Levels() resetar os level

        self.game_model.player = None

        # Iniciar o jogo novamente
        self.start()

    def start(self):
        def play():
            # pygame.mixer.music.play(-1)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        while True:
                            pygame.quit()
                            sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_t:
                            next_level = Level(
                                f"level_{len(self.game_model.levels) + 1}", self.game_model.player
                            )
                            self.game_model.levels.add_level(next_level)
                            self.game_model.advance_level()
                if self.game_model.player == None:
                    self.game_model.player = self.game_model.level_container.get_level().controller.player
                if self.game_model.player.hp == 0:
                    # pygame.mixer.Sound.play(self.game_over_sound)
                    self.game_model.player = None
                    self.choose_view("gameover")

                self.game_model.level_container.get_level().surface.fill("#71ddee")

                # roda fase
                self.game_model.level_container.get_level().run()
                self.input_handler()

                # atualiza display
                pygame.display.flip()

                # define fps do jogo
                self.clock.tick(Settings().fps)

        if self.game_model.player == None:
            play()
        else:
            if self.game_model.player.hp == 0:
                self.reset()
            else:
                play()

    def choose_view(self, name):
        try:
            self.view_container.view = name
            self.view_container.render_view(self)
        except ViewNotFound as exception:
            print(exception)
        except ViewNotRendered as exception:
            print(exception)

    def input_handler(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        controller = self.game_model.level_container.get_level().controller
        player = controller.player
        # movement input
        if player.action == "normal":
            if keys[pygame.K_UP]:
                player.direction.y = -1
                player.status = "up"

            elif keys[pygame.K_DOWN]:
                player.direction.y = 1
            else:
                player.direction.y = 0

            if keys[pygame.K_LEFT]:
                player.direction.x = -1
                player.status = "left"

            elif keys[pygame.K_RIGHT]:
                player.direction.x = 1
            else:
                player.direction.x = 0

        # raid input
        if keys[pygame.K_SPACE]:
            #             if player.inventory.contains("raid") and (not player.attacking):
            #                     if current_time - player.inventory.get("raid").time >= player.inventory.get("raid").cooldown:
            #                         if player.stamina_check(player.inventory.get('raid').stamina_cost):
            pygame.mixer.Sound.play(self.attack_sound)
            #                             player.attacking = True
            #                             player.inventory.get("raid").time = pygame.time.get_ticks()
            #                             controller.create_attack()

            player.create_attack(
                controller.visible_sprites, controller.attacks_sprites, current_time
            )

        # guard input
        #         if keys[pygame.K_LCTRL]:
        #             player.create_defense(controller.visible_sprites, controller.deffense_sprites, controller.obstacles_sprites, current_time)

        #         # dash input
        #         if keys[pygame.K_LSHIFT]:
        #             player.use_dash(current_time)

        # pick input
        if keys[pygame.K_c]:
            pygame.mixer.Sound.play(self.picking_sound)
            player.picking = True
        else:
            player.picking = False

        # guard input
        if keys[pygame.K_LCTRL]:
            if player.inventory.contains("guard"):
                if (
                    current_time - player.inventory.get("guard").time
                    >= player.inventory.get("guard").cooldown
                ):
                    if self.game_model.player.stamina_check(
                        self.game_model.player.inventory.get("raid").stamina_cost
                    ):
                        pygame.mixer.Sound.play(self.guard_sound)
                        player.deffending = True
                        player.inventory.get("guard").time = pygame.time.get_ticks()
                        controller.create_defense()

        # dash input
        if keys[pygame.K_LSHIFT]:
            if player.inventory.contains("dash"):
                try:
                    if (
                        current_time - player.inventory.get("dash").time
                        >= player.inventory.get("dash").cooldown
                    ):
                        pygame.mixer.Sound.play(self.dash_sound)
                        player.use_dash()
                except:
                    player.use_dash()

        if keys[pygame.K_ESCAPE]:
            self.choose_view("menu")
    
    