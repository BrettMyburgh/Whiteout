import pygame
from ..Levels import forest_level_1

class gameplay():
    def __init__(self):
        pass

    def main(self):
        pygame.init()

        #Setup
        screen = pygame.display.set_mode((1280,720))
        clock = pygame.time.Clock()
        running = True
        delta = 0

        camera_offset = pygame.Vector2(0,0)
        world_coords = pygame.Vector2(0,0)

        level = forest_level_1.level(500,500)
        mapping = level.generate_mapping()
        ground = level.generate_map(mapping)
        #Created once

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            bgcolor = 170,170,170
            screen.fill(bgcolor)

            # ground.draw(screen)

            speed = 300 * delta
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                camera_offset.y -= speed
            if keys[pygame.K_s]:
                camera_offset.y += speed
            if keys[pygame.K_a]:
                camera_offset.x -= speed
            if keys[pygame.K_d]:
                camera_offset.x += speed

        # camera_offset.x = player.rect.centerx - screen_width // 2
        # camera_offset.y = player.rect.centery - screen_height // 2

                # pygame move camera
            # for sprite in ground:
            #     screen.blit(sprite.image, sprite.rect.move(-camera_offset.x, -camera_offset.y))

            # screen.blit(ground.sprites.image, ground.sprites.rect.move(-camera_offset.x, -camera_offset.y))
            pygame.display.flip()

            delta = clock.tick(60) / 1000

        pygame.quit()