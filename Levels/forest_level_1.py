import pygame
import sys
import random
from ..Gameplay.sprites import groundSprite
from pygame.sprite import Sprite, Group

class level:

    height = 0
    width = 0

    

    def __init__(self):
        pass

    def generate_map( self):
        map_mapping = []
        for y in range(self.height):
            map_mapping.append(self.get_floor(self.width))

    def get_floor(numbers):
        floors = ["Grass.png","Dirt.png", "Stone.png", "Sand.png","Cobble.png","StoneGrass.png", "Brick.png"]
        weight = [0.6,0.05,0.05,0.05,0.025,0.2,0.025]
        row = random.choices(floors, weights=weight, k=numbers)
        return row
    
    def generate_map(self,mapping):
        x = 0
        y = 0
        map = Group()
        for row in mapping:
            for col in row:
                sprite = groundSprite(x,y,col)
                x = sprite.get_rect().right
                map.add(sprite)


