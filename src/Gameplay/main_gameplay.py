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

        camera_offset = pygame.Vector2(0,0)
        world_coords = pygame.Vector2(0,0)

        #Created once
        level = forest_level_1.level(500,500)
        mapping = level.generate_mapping()
        level.generate_map(mapping)

        player = player_base.player().load_player(screen.width / 2, screen.height / 2)
        
        map = level.load_level()
        for sprite in map:
                if sprite.name == "Ground":
                    screen_center = screen.get_rect().center
                    sprite_rect = sprite.rect
                    sprite_rect.center = screen_center
                    screen.blit(sprite.image, sprite_rect)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            bgcolor = 170,170,170
            screen.fill(bgcolor)

            speed = 300 * delta
            keys = pygame.key.get_pressed()
            moved = False
            if keys[pygame.K_w]:
                camera_offset.y -= speed
                moved = True
            if keys[pygame.K_s]:
                camera_offset.y += speed
                moved = True
            if keys[pygame.K_a]:
                camera_offset.x -= speed
                moved = True
            if keys[pygame.K_d]:
                camera_offset.x += speed
                moved = True

            for sprite in map:
                screen.blit(sprite.image, sprite.rect.move(-camera_offset.x, -camera_offset.y))
            
            if moved:
                player.update()
            else:
                for sprite in player:
                    sprite.reset_animation()
                    
            player.draw(screen)

            pygame.display.flip()

            delta = clock.tick(60) / 1000

        pygame.quit()