import pygame
import sys
import random
from ..Gameplay.sprites import groundSprite
from ..Levels.level_sprite import levelSprite
from pygame.sprite import Sprite, Group

class level:

    height = 0
    width = 0
    def __init__(self, h, w):
        self.width = w
        self.height = h

    def generate_mapping( self):
        map_mapping = []
        for y in range(self.height):
            map_mapping.append(self.get_floor(self.width))
        return map_mapping

    def get_floor(self,numbers):
        floors = ["Grass.png","Dirt.png", "Stone.png", "Sand.png","Cobble.png","StoneGrass.png", "Brick.png"]
        weight = [0.6,0.05,0.05,0.05,0.025,0.2,0.025]
        row = random.choices(floors, weights=weight, k=numbers)
        return row
    
    def generate_map(self,mapping):
        x = 0
        y = 0
        max_width = 0
        map = Group()
        for row in mapping:
            for col in row:
                sprite = groundSprite(x,y,"Floors/" + col)
                x = sprite.get_rect().right
                map.add(sprite)
            y += 16
            max_width = x
            x = 0
        self.save_map(map, max_width, y)
        
    
    def save_map(self, group, width, height):
        save_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        group.draw(save_surface)
        pygame.image.save(save_surface, "level.png")
        del(group)

    def load_level(self):
        sprite = levelSprite(0,0,"level.png")
        sprite.name = "Ground"
        levelGroup = Group()
        levelGroup.add(sprite)
        return levelGroup

