import pygame
import sys
from pathlib import Path

pygame.init()

screen = pygame.display.set_mode((288,512))
fps = pygame.time.Clock()
imagenDeFondo = pygame.image.load(Path(__file__).absolute().parent / "assets/background-day.png")

#Terreno:
imagenTerreno = pygame.image.load(Path(__file__).absolute().parent / "assets/base.png")
posTerrenoX = 0
posTerrenoY = 512 - 112

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Muchas gracias")
            pygame.quit()
            sys.exit()

    screen.blit(imagenDeFondo, (0,0))
    screen.blit(imagenTerreno, (0,0))

    screen.blit(imagenTerreno, (posTerrenoX, posTerrenoY))

    pygame.display.update()
    fps.tick(60)