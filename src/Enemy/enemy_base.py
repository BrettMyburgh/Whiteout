import pygame
from .enemy_sprite import enemySprite

class enemy_base():
    speed = 300

    def __init__(self):
        pass
    
    def create_enemy(self, delta, x, y, group):
        self.delta = delta
        sprite = enemySprite(x,y,"Enemy/Enemy.png",self.speed * delta)
        group.add(sprite)
        return group