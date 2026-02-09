import pygame
from pygame.sprite import Sprite
from pathlib import Path

class enemySprite(Sprite):

    script_dir = Path(__file__).parent
    animate_step = 0
    x = 0
    y = 0
    speed = 0

    def __init__(self, x, y, file_name, speed):
        super().__init__()
        self.image = pygame.image.load(self.script_dir.parent / "Sprites/FreeAssets" / file_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (42,42))
        self.rect = self.image.get_rect()
        self.rect.size = (42,42)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.speed = speed
    
    def get_rect(self):
        return self.rect
    
    def update(self, player):
        dif_x = self.x - player.x
        x_speed = min(abs(dif_x),self.speed)
        if dif_x > 0:
            self.x -= x_speed 
        elif dif_x < 0:
            self.x += x_speed
        dif_y = self.y - player.y
        y_speed = min(abs(dif_y),self.speed)
        if dif_y > 0:
            self.y -= y_speed
        elif dif_y < 0:
            self.y += y_speed

        self.rect.x = self.x
        self.rect.y = self.y