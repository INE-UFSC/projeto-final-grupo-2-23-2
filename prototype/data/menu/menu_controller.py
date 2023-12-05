import pygame
from data.base.controller import Controller
from data.menu.menu_views import MenuViews

from data.utils.exceptions.view_not_found import ViewNotFound


class MenuController(Controller):
    def __init__(self, game_system):
        super().__init__()
        self.__views_container = MenuViews()
        self.__game_system = game_system
        self.__last_click_time = 0

    def show_menu(self, name):
        try:
            self.__views_container.select_view(name)
            self.run()
        except ViewNotFound as exception:
            print(exception)

    def run(self):
        clock = pygame.time.Clock()

        while True:
            self.handle_events()
            self.view.render()

            clock.tick(60)

    def handle_events(self):
        current_time = pygame.time.get_ticks()
        if current_time - 1000 >= self.__last_click_time:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__game_system.close()

                button = self.get_button_clicks(
                    pygame.mouse.get_pos(), pygame.mouse.get_pressed()
                )

                if button is not None:
                    self.__last_click_time = current_time
                    self.handle_button_click(button)

    def get_button_clicks(self, mouse_pos, mouse_pressed):
        for button in self.view.buttons:
            if button.is_pressed(mouse_pos, mouse_pressed):
                return button
        return None

    def handle_button_click(self, button):
        for view_button in self.view.buttons:
            if button.content == view_button.content:
                self.execute_button_action(view_button)

    def execute_button_action(self, button):
        action = button.action
        if action == "game.play()":
            self.__game_system.play()
        elif action == "game.show_menu('introconfig')":
            self.__game_system.show_menu('introconfig')
        elif action == "game.close()":
            self.__game_system.close()

    # Getters and Setters
    @property
    def views_container(self):
        return self.__views_container

    @property
    def game_system(self):
        return self.__game_system

    @property
    def last_click_time(self):
        return self.__last_click_time

    @last_click_time.setter
    def last_click_time(self, new_time):
        self.__last_click_time = new_time

    @property
    def view(self):
        return self.__views_container.view
