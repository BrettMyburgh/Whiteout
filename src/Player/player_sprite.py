import pygame
from pygame.sprite import Sprite
from pathlib import Path

class playerSprite(Sprite):

    script_dir = Path(__file__).parent
    animate_step = 0
    x = 0
    y = 0

    def __init__(self, x, y, file_name, name):
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
        self.name = name
    
    def get_rect(self):
        return self.rect
    
    def update(self):
        self.animate_player()

    def animate_player(self):
        if self.animate_step == 0:
            self.rect.x += 5
            self.rect.y += 5
        elif self.animate_step == 1:
            self.rect.x += 5
            self.rect.y -= 5
        elif self.animate_step == 2:
            self.rect.x -= 5
            self.rect.y += 5
        elif self.animate_step == 3:
            self.rect.x -= 5
            self.rect.y -= 5
        elif self.animate_step == 4:
            self.rect.x -= 5
            self.rect.y += 5
        elif self.animate_step == 5:
            self.rect.x -= 5
            self.rect.y -= 5
        elif self.animate_step == 6:
            self.rect.x += 5
            self.rect.y += 5
        elif self.animate_step == 7:
            self.rect.x += 5
            self.rect.y -= 5
            self.animate_step = -1
        self.animate_step += 0.25

    def reset_animation(self):
        self.animate_step = 0
        self.rect.x = self.x
        self.rect.y = self.y

    def check_collision(self, group):
        for sprite in group:
            if "landscape" in sprite.name:
                offset_x = sprite.rect.x - self.rect.x
                offset_y = sprite.rect.y - self.rect.y
                offset = (offset_x, offset_y)
                overlap = self.mask.overlap(sprite.mask, offset)
                if overlap is not None:
                    bottom_height = self.rect.bottom - self.rect.y
                    right = self.rect.right - self.rect.x
                    threshold = 10
                    directions_blocked = ""
                    if bottom_height - overlap[1] < threshold:
                        directions_blocked = "bottom_" + str(bottom_height - overlap[1])
                    if overlap[1] < threshold:
                        directions_blocked = "top_" + str(overlap[1])

                    if overlap[0] < threshold:
                        directions_blocked = "left_" + str(overlap[0])
                    if right - overlap[0] < threshold:
                        directions_blocked = "right_" + str(right - overlap[0])
                    return directions_blocked
        return None

    def prevent_overlap(self, sprite):
        bounding_recs = self.mask.get_bounding_rects()
        sprite_bounding_recs = sprite.mask.get_bounding_rects()
        test = ""
