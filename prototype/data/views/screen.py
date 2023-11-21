import pygame

class Screen:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.width = self.game.width
        self.height = self.game.height

        self.background = pygame.image.load("prototype/resources/graphics/menu_graphics/intros/intro2.png")
        
        self.font = pygame.font.Font('stocky.ttf', 32)
        self.title = self.font.render('Parts Finder', True, (255,255,255))
        self.title_rect = self.title.get_rect(x = self.game.width/2 - 130, y = 10)
        
        self.buttons = self.get_buttons()


        
        self.wait_time = 300
        self.primary = True

    def get_buttons(self):
        pass

    def get_button_clicks(self, mouse_pos, mouse_pressed):
        for button in self.buttons:
            if button.is_pressed(mouse_pos, mouse_pressed):
                return button    
        return None

    def blit(self):
        self.game.view.blit(self.background, (0,0))
        self.game.view.blit(self.title, self.title_rect)

        for button in self.buttons:
            self.game.view.blit(button.image, button.rect)

        pygame.display.flip()
        self.game.clock.tick(self.game.fps)

