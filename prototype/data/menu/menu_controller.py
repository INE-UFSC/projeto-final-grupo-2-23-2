import pygame
from data.base.controller import Controller
from data.menu.menu_views import MenuViews
from data.menu.gameover_view import GameoverView
from data.menu.intro_config_view import IntroconfigView
from data.menu.intro_view import IntroView
from data.menu.pause_config_view import PauseconfigView
from data.menu.pause_view import PauseView



class MenuController(Controller):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.views_container = MenuViews()  

        self.__add_views()      

    def show_menu(self, name):
        if self.views_container.select_view(name):
            self.run()

    def run(self):
        clock = pygame.time.Clock()
        self.last_click_time = 0

        while True:
            self.handle_events()
            self.view.render()

            clock.tick(30)
    

    def handle_events(self):
        current_time = pygame.time.get_ticks()
        if current_time - 1000 >= self.last_click_time:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.close()

                button = self.get_button_clicks(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

                if button is not None:
                    self.last_click_time = current_time
                    self.handle_button_click(button)

    def get_button_clicks(self, mouse_pos, mouse_pressed):
        for button in self.view.buttons:
            if button.is_pressed(mouse_pos, mouse_pressed):
                return button    
        return None
    
    def handle_button_click(self, button):
        for view_button in self.view.buttons:
            if button.content == view_button.content:
                exec(view_button.action, {"game": self.game})
    
    @property
    def view(self):
        return self.views_container.view
    
    def __add_views(self):
        self.views_container.add_view(GameoverView())
        self.views_container.add_view(IntroconfigView())
        self.views_container.add_view(IntroView())
        self.views_container.add_view(PauseconfigView())
        self.views_container.add_view(PauseView())

