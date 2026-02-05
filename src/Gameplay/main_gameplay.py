import pygame
from ..Levels import forest_level_1
from ..Player import player_base

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
        can_move_up = True
        can_move_down = True
        can_move_left = True
        can_move_right = True

        camera_offset = pygame.Vector2(0,0)
        world_coords = pygame.Vector2(0,0)

        #Created once
        level = forest_level_1.level(500,500)
        # level = forest_level_1.level(50,50)
        mapping = level.generate_mapping()
        level.generate_map(mapping)

        player = player_base.player().load_player(screen.width / 2, screen.height / 2)
        
        map = level.load_level()
        for sprite in map:
                if sprite.name == "Ground":
                    screen_center = screen.get_rect().center
                    # camera_offset = pygame.Vector2(screen_center[0],screen_center[1]) 
                    sprite_rect = sprite.rect
                    sprite_rect.center = screen_center
                    camera_offset = pygame.Vector2(-sprite_rect.x/2,-sprite_rect.y/2) 
                    sprite.update(-camera_offset.x, -camera_offset.y)
                    screen.blit(sprite.image, sprite_rect)
                    level_obstacles = 500
                    map = level.load_opjects(sprite_rect.top, sprite_rect.left, sprite_rect.bottom, sprite_rect.right, map, level_obstacles)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            bgcolor = 170,170,170
            screen.fill(bgcolor)

            camera_offset = pygame.Vector2(0,0)

            speed = 300 * delta
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
                can_move_up = True
                can_move_down = True
                can_move_left = True
                can_move_right = True
                new_rect = pygame.Rect(-camera_offset.x, -camera_offset.y,0,0)
                collide = False
                for sprite in player:
                    if sprite.name == "base":
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
                for sprite in map:
                    # if collide:
                    #     new_rect = sprite.rect.move(-camera_offset.x + new_rect.x, -camera_offset.y + new_rect.y)
                    # else:
                    new_rect = sprite.rect.move(-camera_offset.x, -camera_offset.y)
                
                    sprite.update(new_rect.x, new_rect.y)
            for sprite in map:
                screen.blit(sprite.image, sprite.rect)
            if moved:
                player.update()
            else:
                for sprite in player:
                    sprite.reset_animation()
                    
            player.draw(screen)

            pygame.display.flip()

            delta = clock.tick(60) / 1000

        pygame.quit()