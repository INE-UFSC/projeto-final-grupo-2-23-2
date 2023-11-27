from data.base.controller import Controller
from data.menu.menu_views import MenuViews
from data.game.game_model import GameModel
from data.game.game_view import GameView
from data.components.settings import Settings
from data.game.level import Level
import pygame
import sys

class GameController(Controller):
    def __init__(self, game_system):
        super().__init__()
        self.game_view = GameView()
        self.game_model = GameModel()
        self.game_system = game_system

    def play(self):
        if self.game_model.player is None or self.game_model.player.hp == 0:
            self.reset()
        self.run()

    def reset(self):
        self.game_model.reset()

    def run(self):
        # pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    while True:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        self.game_model.levels_container.advance_level()
                        
            if self.game_model.player == None:
                self.game_model.player = self.game_model.levels_container.get_level().controller.player

            if self.game_model.player.hp == 0:
                # pygame.mixer.Sound.play(self.game_over_sound)
                self.game_model.player = None
                self.game_system.show_menu("gameover")

            self.game_model.levels_container.get_level().surface.fill("#71ddee")

            # roda fase
            self.game_model.levels_container.get_level().run()
            self.input_handler()

            # atualiza display
            self.game_view.render()

            # define fps do jogo
            clock.tick(Settings().fps)



    def input_handler(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        controller = self.game_model.levels_container.get_level().controller
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
            # pygame.mixer.Sound.play(self.attack_sound)
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
            # pygame.mixer.Sound.play(self.picking_sound)
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
            self.game_system.show_menu("pause")