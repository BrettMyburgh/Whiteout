import pygame
import sys
import random
from ..Gameplay.sprites import groundSprite
from .level_sprite import levelSprite
from .landscape_sprite import landscapeSprite
from pygame.sprite import Group
import os

class level:

    height = 0
    width = 0
    def __init__(self, h, w):
        self.width = w
        self.height = h

    def generate_mapping( self):
        #Create random map
        map_mapping = []
        for y in range(self.height):
            map_mapping.append(self.get_floor(self.width))
        return map_mapping

    def get_floor(self,numbers):
        #Weighted random floors
        floors = ["Grass.png","Dirt.png", "Stone.png", "Sand.png","Cobble.png","StoneGrass.png", "Brick.png"]
        weight = [0.6,0.05,0.05,0.05,0.025,0.2,0.025]
        row = random.choices(floors, weights=weight, k=numbers)
        return row
    
    def generate_map(self,mapping):
        #Uses mappings to create 1 map sprite for performance
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

    def load_opjects(self,start_x, start_y, end_x,end_y,group, count):
        #Load landscape items
        for i in range(count):
            random_x = random.randint(start_x + 20, end_x-20)
            random_y = random.randint(start_y + 20, end_y -20)
            directory = "src/Sprites/FreeAssets/Landscape/Forest/"
            landscape_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and "Top" not in f]
            landscape_file = random.choice(landscape_list)
            landscape_item = landscapeSprite(random_x, random_y, directory + landscape_file, str(i))
            group.add(landscape_item)
            if "Bottom" in landscape_file:
                landscape_rect = landscape_item.rect
                top_right = landscape_rect.topright
                landscape_item_top = landscapeSprite(top_right[0]-42, top_right[1]-42, directory + landscape_file.replace("Bottom", "Top"), str(i)+"top")
                landscape_item_top_rect = landscape_item_top.rect
                landscape_item_top_rect.bottomright = top_right
                group.add(landscape_item_top)
        return group
