import pygame
from pygame.sprite import Sprite
from pathlib import Path
from .enemy_attack_sprite import enemyAttackSprite

class enemySprite(Sprite):

    script_dir = Path(__file__).parent
    animate_step = 0
    x = 0
    y = 0
    speed = 0
    can_move_up = True
    can_move_down = True
    can_move_left = True
    can_move_right = True
    name = "enemy"

    def __init__(self, x, y, file_name, speed, tranparent_screen):
        super().__init__()
        #Create enemy sprite and scale
        self.image = pygame.image.load(self.script_dir.parent / "Sprites/FreeAssets" / file_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (42,42))
        self.rect = self.image.get_rect()
        self.rect.size = (42,42)
        self.mask = pygame.mask.from_surface(self.image)
        self.attack_sprite = enemyAttackSprite(self.rect.centerx, self.rect.centery, tranparent_screen)

        #Position and set speed
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.speed = speed
    
    def get_rect(self):
        return self.rect
    
    def update(self, player, screen_x, screen_y, ground, enemies):
        #Get X movement
        dif_x = self.x - player.x

        #Prevent flicker on x
        x_speed = min(abs(dif_x),self.speed) 

        #move enemy on x
        if dif_x > 0 and self.can_move_left:
            self.x -= x_speed
        elif dif_x < 0 and self.can_move_right:
            self.x += x_speed
        else:
            self.x += x_speed

        #Get Y Movement
        dif_y = self.y - player.y

        #Prevent flicker on Y
        y_speed = min(abs(dif_y),self.speed)

        #Move enemy on Y
        if dif_y > 0 and self.can_move_up:
            self.y -= y_speed
        elif dif_y < 0 and self.can_move_down:
            self.y += y_speed
        else:
            self.y -= y_speed

        #Reset can move
        self.can_move_up = True
        self.can_move_down = True
        self.can_move_left = True
        self.can_move_right = True

        #Check collision with landscape
        colision_location = self.check_collision_with_mask(ground)
        if colision_location is not None:
            colision_location_split = colision_location.split("_")
            match colision_location_split[0]:
                case "left":
                    if self.x > 0:
                        #Move back to prevent overlap
                        self.x += int(colision_location_split[1])
                        #Can't move that direction
                        self.can_move_left = False
                case "right":
                    if self.x > 0:
                        #Move back to prevent overlap
                        self.x -= int(colision_location_split[1])
                        #Can't move that direction
                        self.can_move_right = False
                case "top":
                    if self.y > 0:
                        #Move back to prevent overlap
                        self.y += int(colision_location_split[1])
                        #Can't move that direction
                        self.can_move_up = False
                case "bottom":
                    if self.y > 0:
                        #Move back to prevent overlap
                        self.y -= int(colision_location_split[1])
                        #Can't move that direction
                        self.can_move_down = False

        #Check collision with other enemies
        colision_location = self.check_collision_with_mask(enemies)
        if colision_location is not None:
            colision_location_split = colision_location.split("_")
            match colision_location_split[0]:
                case "left":
                    if self.x > 0:
                        #Move back to prevent overlap
                        self.x += int(colision_location_split[1])
                        #Can't move that direction
                        self.can_move_left = False
                case "right":
                    if self.x > 0:
                        #Move back to prevent overlap
                        self.x -= int(colision_location_split[1])
                        #Can't move that direction
                        self.can_move_right = False
                case "top":
                    if self.y > 0:
                        #Move back to prevent overlap
                        self.y += int(colision_location_split[1])
                        #Can't move that direction
                        self.can_move_up = False
                case "bottom":
                    if self.y > 0:
                        #Move back to prevent overlap
                        self.y -= int(colision_location_split[1])
                        #Can't move that direction
                        self.can_move_down = False

        #Move enemy based on "Camera" move
        self.x += screen_x
        self.y += screen_y

        #Set movement to rect
        self.rect.x = self.x
        self.rect.y = self.y

        self.attack_sprite.update(self.rect.centerx, self.rect.centery)

        #Temp to remove
        self.check_colision(player)
        
    def attack_draw(self, screen,transparent_screen):
        self.attack_sprite.draw(screen,transparent_screen)

    def check_colision(self, player):
        if self.rect.colliderect(player.rect):
            self.kill()

    def check_collision_with_mask(self, group):
        for sprite in group:
            #check enemy collides with landscape or enemy that is not itself
            if "landscape" in sprite.name or "enemy" in sprite.name and sprite is not self:
                #Offset from top right
                offset_x = sprite.rect.x - self.rect.x
                offset_y = sprite.rect.y - self.rect.y
                offset = (offset_x, offset_y)

                #Get overlap
                overlap = self.mask.overlap(sprite.mask, offset)
                if overlap is not None:
                    #Get bottom and right coordinates
                    bottom_height = self.rect.bottom - self.rect.y
                    right = self.rect.right - self.rect.x
                    threshold = 10
                    directions_blocked = ""
                    #if collision is on bottom
                    if bottom_height - overlap[1] < threshold:
                        directions_blocked = "bottom_" + str(bottom_height - overlap[1])
                    
                    # collision on top
                    if overlap[1] < threshold:
                        directions_blocked = "top_" + str(overlap[1])

                    #collided left side
                    if overlap[0] < threshold:
                        directions_blocked = "left_" + str(overlap[0])
                    
                    #collided right side
                    if right - overlap[0] < threshold:
                        directions_blocked = "right_" + str(right - overlap[0])

                    return directions_blocked
        return None