import pygame
import json
import os
from data.components.player import Player
from data.components.enemy import Enemy
from data.components.enemy_container import EnemyContainer
from data.components.weapon import Weapon

class Level:
    # todo: name_fase != map_name?
    def __init__(self, map_name):
        self.__name = map_name
        self.__map = self.__extract_map(map_name)
        self.__player = None
        self.__enemies = EnemyContainer()

        # pega a surface(tela) que ja existe
        self.surface = pygame.display.get_surface()

        # todos os sprites e sprites que colidem
        self.__visible_sprites = YSortCameraGroup()
        self.__obstacles_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        self.attacks_sprites = pygame.sprite.Group()
        
        # todo: melhor localizacao
        self.__tilesize = 64

        self.__song = None  # name_song
        self.__dropped_items = None  # dropped_items

        self.current_attack = None

        self.generate_map()

    # getters e setters
    @property
    def name(self):
        return self.__name

    @property
    def map(self):
        return self.__map

    @map.setter
    def map(self, map):
        self.__map = map
    
    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        self.__player = player

    @property
    def song(self):
        return self.__song

    @property
    def enemies(self):
        return self.__enemies

    @property
    def dropped_items(self):
        return self.__dropped_items

    @property
    def tilesize(self):
        return self.__tilesize

    @property
    def surface(self):
        return self.__surface

    @surface.setter
    def surface(self, surface):
        self.__surface = surface

    @property
    def visible_sprites(self):
        return self.__visible_sprites

    @visible_sprites.setter
    def visible_sprites(self, visible_sprites):
        self.__visible_sprites = visible_sprites

    @property
    def obstacles_sprites(self):
        return self.__obstacles_sprites

    @obstacles_sprites.setter
    def obstacles_sprites(self, obstacles_sprites):
        self.__obstacles_sprites = obstacles_sprites

    # todo: tratamento de excessoes try
    def __extract_map(self, map_name):
        file_name = os.path.dirname(os.path.abspath(
            __file__)) + "/../../resources/map_data/" + map_name + ".json"
        # Carregando o map a partir do file JSON
        with open(file_name, 'r') as file:
            return json.load(file)

    def generate_map(self):
        # loop pela matriz
        for lin_index, lin in enumerate(self.map):
            for col_index, col in enumerate(lin):
                x = col_index * self.tilesize
                y = lin_index * self. tilesize
                if col == 'x':
                    Tile("tree", (x, y), [
                         self.visible_sprites, self.obstacles_sprites])
                elif col == 'p':
                    self.player = Player(
                        "player", 100, (x, y), [self.visible_sprites], self.visible_sprites, self.obstacles_sprites,self.create_attack,self.destroy_attack)
                elif col == 'i':
                    self.enemy = Enemy(
                        "enemy", 100, (x, y), [self.visible_sprites,self.attackable_sprites], self.visible_sprites, self.obstacles_sprites)

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites,self.attacks_sprites])
        
    def destroy_attack(self):
        if self.current_attack != None:
            self.current_attack.kill()
            self.current_attack = None

    def player_attack_logic(self):
        if self.attacks_sprites:
            for sprites_ataque in self.attacks_sprites:
                collision_sprites = pygame.sprite.spritecollide(sprites_ataque,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                            if target_sprite.hp == 0:
                                target_sprite.kill()
                            else:
                                target_sprite.take_damage(self.player.damage)

        
    def run(self):
        # desenha e atualiza o jogo
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()

# todo : tratamento
class Tile(pygame.sprite.Sprite):
    def __init__(self, name, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.dirname(os.path.abspath(
            __file__)) + '/../../resources/graphics/objects/' + name + '.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -20)

# agrupa todos os sprites visiveis alem de custom_draw pelo y
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # inicializacao
        super().__init__()
        self.surface = pygame.display.get_surface()

        self.half_width = self.surface.get_size()[0] // 2
        self.half_heigth = self.surface.get_size()[1] // 2
        # desvia o map em referencia a tela
        self.offset = pygame.math.Vector2( )

    # praticamente um draw()
    def custom_draw(self, player):
        self.player = player

        # calculando offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_heigth

        # desenhando
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.surface.blit(sprite.image, offset_position)
            
    def enemy_update(self,player):

#         enemies_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'name') and sprite.name == 'enemy']

        enemies_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'name') and sprite.sprite_type == 'enemy']

        for enemy in enemies_sprites:
            enemy.enemy_update(player)
