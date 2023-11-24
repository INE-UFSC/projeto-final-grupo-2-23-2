import pygame

class Settings:

    _instance = None

    def __init__(self):
        self.difficulty = None
        self.clock = pygame.time.Clock()
        self.fps = 60

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance