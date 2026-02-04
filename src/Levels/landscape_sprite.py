import pygame
from pygame.sprite import Sprite
from pathlib import Path

class landscapeSprite(Sprite):

    script_dir = Path(__file__).parent

    def __init__(self, x, y, file_name):
        super().__init__()
        self.image = pygame.image.load(file_name).convert_alpha()
        self.rect = self.image.get_rect()
        # self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.name = "landscape"
    
    def get_rect(self):
        return self.rect
    
    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y