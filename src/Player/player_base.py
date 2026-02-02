import pygame
from player_sprite import playerSprite

class player:

    def __init__(self):
        pass

    def load_player(self, screenx, screeny):
        sprite = playerSprite(screenx,screeny,"Character/" + "Char1.png")