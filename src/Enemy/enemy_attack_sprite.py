import pygame
from pygame.sprite import Sprite
from pathlib import Path

class enemyAttackSprite(Sprite):
    def __init__(self, x, y, transparent_screen):
        super().__init__()
        self.rect = pygame.draw.circle(transparent_screen, (0, 0, 0, 0), (x, y), 50, width = 2)

    def draw(self, screen,transparent_screen):
        self.rect = pygame.draw.circle(transparent_screen, (255, 255, 255, 150), (self.rect.centerx, self.rect.centery), 50, width = 2)
        screen.blit(transparent_screen,(0,0))
        # del(self.last_circle)

    def update(self, x,y):
        self.rect.centerx = x
        self.rect.centery = y