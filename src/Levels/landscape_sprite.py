import pygame
from pygame.sprite import Sprite
from pathlib import Path

class landscapeSprite(Sprite):

    script_dir = Path(__file__).parent

    def __init__(self, x, y, file_name, sprite_name):
        super().__init__()
        self.image = pygame.image.load(file_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (42,42))
        self.rect = self.image.get_rect()
        self.rect.size = (42,42)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.name = "landscape_" + sprite_name
    
    def get_rect(self):
        return self.rect
    
    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y