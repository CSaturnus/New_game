import pygame
import numpy as np
from perlin_noise import PerlinNoise
import random

pygame.init()

WIDTH, HEIGHT = 1000, 1000
TILE_SIZE = 10
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower_sim")

class GeneratedMap:
    def __init__(self, xpix, ypix, octaves=4, seed=1):
        np.random.seed(seed)
        self.xpix = xpix
        self.ypix = ypix
        self.noise = PerlinNoise(octaves=octaves, seed=seed)

        # Generate Perlin noise values and normalize them to 0-255
        self.pic = np.array([[self.noise([i / xpix, j / ypix]) for j in range(ypix)] for i in range(xpix)])
        self.pic = (self.pic - self.pic.min()) / (self.pic.max() - self.pic.min()) * 255  # Normalize to 0-255
    
    def draw(self, screen):
        for i in range(self.xpix):
            for j in range(self.ypix):
                value = self.pic[i][j]  # Get pixel intensity

                if value <= 100:
                    scale = value / 100
                    if scale < 0.3 :
                        scale = 0.3
                    color = (0, int(84 * scale), int(119 * scale))
                elif 100 < value <= 122:
                    scale = value / 122
                    color = (int(211*scale), int(192*scale), int(157*scale))
                elif 122 < value <= 255:
                    scale = value / 190
                    color = (int(86/scale), int(125/scale), int(70/scale))

                pygame.draw.rect(screen, color, (i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE))


def main():
    
    running = True
    clock = pygame.time.Clock()

    xpix, ypix, octaves, seed = 100, 100, 3, random.randint(1, 1000)
    map = GeneratedMap(xpix, ypix, octaves, seed)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        map.draw(screen)

        pygame.display.update()
        clock.tick(FPS)
        
if __name__ == '__main__':
    main()
pygame.quit()