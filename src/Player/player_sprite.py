import pygame
from pygame.sprite import Sprite
from pathlib import Path

class playerSprite(Sprite):

    script_dir = Path(__file__).parent
    animate_step = 0
    x = 0
    y = 0

    def __init__(self, x, y, file_name):
        super().__init__()
        self.image = pygame.image.load(self.script_dir.parent / "Sprites/FreeAssets" / file_name)
        self.image = pygame.transform.scale(self.image, (42,42))
        self.rect = self.image.get_rect()
        self.rect.size = (42,42)
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
    
    def get_rect(self):
        return self.rect
    
    def update(self):
        self.animate_player()

    def animate_player(self):
        if self.animate_step == 0:
            self.rect.x += 5
            self.rect.y += 5
        elif self.animate_step == 1:
            self.rect.x += 5
            self.rect.y -= 5
        elif self.animate_step == 2:
            self.rect.x -= 5
            self.rect.y += 5
        elif self.animate_step == 3:
            self.rect.x -= 5
            self.rect.y -= 5
        elif self.animate_step == 4:
            self.rect.x -= 5
            self.rect.y += 5
        elif self.animate_step == 5:
            self.rect.x -= 5
            self.rect.y -= 5
        elif self.animate_step == 6:
            self.rect.x += 5
            self.rect.y += 5
        elif self.animate_step == 7:
            self.rect.x += 5
            self.rect.y -= 5
            self.animate_step = -1
        self.animate_step += 0.25

    def reset_animation(self):
        self.animate_step = 0
        self.rect.x = self.x
        self.rect.y = self.y