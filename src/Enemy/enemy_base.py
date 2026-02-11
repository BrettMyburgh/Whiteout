import pygame
from .enemy_sprite import enemySprite

class enemy_base():
    speed = 200

    def __init__(self):
        pass
    
    def create_enemy(self, delta, x, y, group):
        #spawn new enemy and add to the group
        self.delta = delta
        sprite = enemySprite(x,y,"Enemy/Enemy.png",self.speed * delta)
        group.add(sprite)
        return group