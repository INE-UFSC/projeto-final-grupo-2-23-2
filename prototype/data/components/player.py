from data.components.creature import Creature
import pygame
import os

class Player(Creature):
    def __init__(self, name, hp, position, groups, visible_sprites, obstacle_sprites, generate_attack, destroy_attack):
        super().__init__(name, hp, position, groups, visible_sprites, obstacle_sprites)
        
        # todo: analisar heranca inimigo jogador
        self.__image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__))+'/../../resources/graphics/player/' + name + '.png').convert_alpha()
        self.__rect = self.image.get_rect(topleft=position)
        self.__hitbox = self.__rect.inflate(0, -26)

        #caracteristicas do player
        self.status = 'down'
        self.attacking = False
        self.attack_time = None
        self.attack_cooldown = 250
        self.ratio_health_bar = hp / 200 # tamanho da barra
        self.damage = 5
        
        #metodos vindos de fase
        self.generate_attack = generate_attack
        self.destroy_attack = destroy_attack
        self.sprite_type = 'player'
        
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.attacking == False:
            self.direction.y = -1   
            self.status = 'up'

        elif keys[pygame.K_DOWN] and self.attacking == False:
            self.direction.y = 1  
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT] and self.attacking == False:
            self.direction.x = -1
            self.status = 'left'

        elif keys[pygame.K_RIGHT] and self.attacking == False:
            self.direction.x = 1
            self.status = 'rigth'
        else:
            self.direction.x = 0
            
        if keys[pygame.K_SPACE]:
            if not self.attacking:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.generate_attack()

    def update(self):
        self.input()
        self.move()
        self.cooldowns()
        self.health_bar()
    
    def cooldowns(self):
        tempo_atual = pygame.time.get_ticks()
        if self.attacking:
            if tempo_atual - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()

    # gambiarra
    def health_bar(self):
        sv = self.visible_sprites
        pygame.draw.rect(sv.surface, (255, 0, 0), (10, 10, self.hp/self.ratio_health_bar, 20))
        pygame.draw.rect(sv.surface, (255, 255, 255), (10, 10, 200, 20),4)

    # getters e setters
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, image):
        self.__image = image
    
    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, rect):
        self.__rect = rect
    
    @property
    def hitbox(self):
        return self.__hitbox
    
    @rect.setter
    def hitbox(self, hitbox):
        self.__hitbox = hitbox


