import pygame
from .player_sprite import playerSprite
from pygame.sprite import Group
import os
import random

class player:

    def __init__(self):
        pass

    def load_player(self, screenx, screeny):
        sprite = playerSprite(screenx,screeny,"Character/" + "Char1.png", "base")
        player = Group()
        player.add(sprite)
        player = self.accessories(screenx, screeny, player)
        return player
    
    def accessories(self, x, y, player_group):
        hair_count = 0
        beard_count = 0
        directory = "src/Sprites/FreeAssets/Character/Accessories/"
        hair_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and "Hair" in f]
        beard_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and "Beard" in f]
        if random.randint(0,10) > 5:
            beard_file = self.get_random_file(beard_list)
            sprite = playerSprite(x,y,"Character/Accessories/" + beard_file, "accessory")
            player_group.add(sprite)
        hair_file = self.get_random_file(hair_list)
        hair_sprite = playerSprite(x,y,"Character/Accessories/" + hair_file, "accessory")
        player_group.add(hair_sprite)
        return player_group

            

    def get_random_file(self, file_list):
        file_name = random.choice(file_list)
        return file_name


