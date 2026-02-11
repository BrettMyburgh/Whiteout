import pygame
from ..Levels import forest_level_1
from ..Player import player_base
from ..Enemy import enemy_base
from pygame.sprite import Group
import random

class gameplay():
    def __init__(self):
        pass

    def main(self):
        pygame.init()

        #Setup
        screen = pygame.display.set_mode((1280,720), pygame.SCALED, vsync=True)
        clock = pygame.time.Clock()
        running = True
        delta = 0

        #Player
        can_move_up = True
        can_move_down = True
        can_move_left = True
        can_move_right = True
        player = player_base.player().load_player(screen.width / 2, screen.height / 2)

        #Screen movement
        camera_offset = pygame.Vector2(0,0)

        #Map
        level = forest_level_1.level(500,500)
        mapping = level.generate_mapping()
        level.generate_map(mapping)
        map = level.load_level()
        #Center Map
        for sprite in map:
                if sprite.name == "Ground":
                    screen_center = screen.get_rect().center
                    sprite_rect = sprite.rect
                    sprite_rect.center = screen_center
                    camera_offset = pygame.Vector2(-sprite_rect.x/2,-sprite_rect.y/2) 
                    sprite.update(-camera_offset.x, -camera_offset.y)
                    screen.blit(sprite.image, sprite_rect)
                    level_obstacles = 500
                    map = level.load_opjects(sprite_rect.top, sprite_rect.left, sprite_rect.bottom, sprite_rect.right, map, level_obstacles)
        
        #Enemy
        enemy_count = 10
        enemies = Group()
        
        #Game loop
        while running:
            #Check for quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            #backgroud
            bgcolor = 170,170,170
            screen.fill(bgcolor)

            #Camera setup
            camera_offset = pygame.Vector2(0,0)
            speed = 300 * delta

            #Enemy Generation
            if len(enemies) < enemy_count and delta > 0 and delta < 1:
                location = self.random_edge_point(screen)
                enemies = enemy_base.enemy_base().create_enemy(delta,location[0], location[1],enemies)

            #Movement
            keys = pygame.key.get_pressed()
            moved = False
            if keys[pygame.K_w] and can_move_up:
                camera_offset.y -= speed
                moved = True
            if keys[pygame.K_s] and can_move_down:
                camera_offset.y += speed
                moved = True
            if keys[pygame.K_a] and can_move_left:
                camera_offset.x -= speed
                moved = True
            if keys[pygame.K_d] and can_move_right:
                camera_offset.x += speed
                moved = True

            if moved:
                #Player Movement
                can_move_up = True
                can_move_down = True
                can_move_left = True
                can_move_right = True
                new_rect = pygame.Rect(-camera_offset.x, -camera_offset.y,0,0)
                for sprite in player:
                    if sprite.name == "base":
                        #Player collision with environment
                        colliding_sprite = sprite.check_collision(map)
                        if colliding_sprite is not None:
                            if "top" in colliding_sprite:
                                can_move_up = False
                                camera_offset.y = camera_offset.y + int(colliding_sprite.split("_")[1])
                            elif "bottom" in colliding_sprite:
                                can_move_down = False
                                camera_offset.y = camera_offset.y - int(colliding_sprite.split("_")[1])
                            elif "left" in colliding_sprite:
                                can_move_left = False
                                camera_offset.x = camera_offset.x + int(colliding_sprite.split("_")[1])
                            elif "right" in colliding_sprite:
                                can_move_right = False
                                camera_offset.x = camera_offset.x - int(colliding_sprite.split("_")[1])
                player.update()

                #Map movement
                for sprite in map:
                    new_rect = sprite.rect.move(-camera_offset.x, -camera_offset.y)
                
                    sprite.update(new_rect.x, new_rect.y)
            else:
                #Animation cancel if no move
                for sprite in player:
                    sprite.reset_animation()

            #Enemy movement
            enemies.update(player.sprites()[0], -camera_offset.x, -camera_offset.y, map,enemies)

            #Drawing
            for sprite in map:
                screen.blit(sprite.image, sprite.rect)
            enemies.draw(screen)
            player.draw(screen)

            pygame.display.flip()

            delta = clock.tick(60) / 1000

        pygame.quit()
    
    def random_edge_point(self, screen):
        #Get random point at edge of screen
        top_left = random.randint(1,4)
        location = pygame.Vector2(0,0)
        match top_left:
            case 1:
                location[1] = random.randint(0,screen.width)
            case 2:
                location[0] = screen.height
                location[1] = random.randint(0,screen.width)
            case 3:
                location[1] = 0
                location[0] = random.randint(0,screen.height)
            case 4:
                location[1] = screen.width
                location[0] = random.randint(0,screen.height)

        return location