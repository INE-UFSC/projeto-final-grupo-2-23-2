import pygame

class Arma(pygame.sprite.Sprite):
    def __init__(self,player, grupos):
        super().__init__(grupos)
        direcao = player.status.split(' ')[0]
        self.image = pygame.Surface((40,40))
        self.rect = self.image.get_rect(center = player.rect.center)
        
        if direcao == 'direita':
            self.rect = self.image.get_rect(midleft = player.rect.midright)
            
        elif direcao == 'esquerda':
            self.rect = self.image.get_rect(midright = player.rect.midleft)

        elif direcao == 'baixo':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom)
            
        else:
            self.rect = self.image.get_rect(midbottom = player.rect.midtop)