import pygame
import sys
from data.components.creatures.player import Player
from data.components.containers.level_container import LevelContainer
from data.components.containers.level import Level
from data.views.view_container import ViewContainer


class Game:
    def __init__(self):
        # inciando pygame
        pygame.init()

        # atributos
        self.__player = None #todo: tem que ficar aqui?
        self.__difficulty = None
        self.__views = ViewContainer()

        # vai pra na tela depois, todo: nao vimos mvcnho
        self.__width = 1280
        self.__heigth = 768
        self.__fps = 60
        self.__clock = pygame.time.Clock()
        self.view = pygame.display.set_mode((self.__width, self.__heigth))
        pygame.display.set_caption('PartsFinder')
        #

        # demais atributos
        self.__levels = LevelContainer()
        self.__current_level = self.levels.get_level()

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
            if self.current_level.player.hp == 0:
                pygame.quit()

            # prenchendo display com verde, reseta a malha
            self.current_level.surface.fill('darkgreen')

            # roda fase
            self.current_level.run()

            # atualiza display
            pygame.display.update()

            # define fps do jogo
            self.__clock.tick(self.__fps)

    def menu_principal(self):
        pass

    
        
    # getters e setters
    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        self.__player = player

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        self.__difficulty = difficulty

    @property
    def views(self):
        return self.__views

    @property
    def levels(self):
        return self.__levels

    @property
    def current_level(self):
        return self.__current_level

    @current_level.setter
    def current_level(self, current_level):
        self.__current_level = current_level
