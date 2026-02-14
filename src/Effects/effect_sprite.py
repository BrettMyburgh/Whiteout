import pygame
from pygame.sprite import Sprite
from pathlib import Path

class playerAttackSprite(Sprite):
    def __init__(self, x, y, transparent_screen):
        super().__init__()
        self.rect = pygame.draw.circle(transparent_screen, (0, 0, 0, 0), (x+21, y+21), 50, width = 2)

    def draw(self, screen,transparent_screen):
        pygame.draw.circle(transparent_screen, (255, 255, 255, 150), (self.rect.centerx, self.rect.centery), 50, width = 2)
        screen.blit(transparent_screen,(0,0))

    def check_collision(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                #enemy entered attack range
                pass