import pygame
import sys
from pathlib import Path

pygame.init()

screen = pygame.display.set_mode((288,512))
fps = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Muchas gracias")
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(60)