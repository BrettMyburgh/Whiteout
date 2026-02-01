import pygame
from pygame.sprite import Sprite, Group
from pathlib import Path

class groundSprite(Sprite):

    script_dir = Path(__file__).parent

    def __init__(self, x, y, col):
        super().__init__()
        self.image = pygame.image.load(self.script_dir.parent / "Sprites/FreeAssets/Floors" / col)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def get_rect(self):
        return self.rect
    
    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y