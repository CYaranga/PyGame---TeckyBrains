import pygame
import sys
from pathlib import Path

pygame.init()

screen = pygame.display.set_mode((288,512))
fps = pygame.time.Clock()
imagenDeFondo = pygame.image.load(Path(__file__).absolute().parent / "assets/background-day.png")

#Personaje:
gravedad = 0.1
velocidadPersonajeY = 0
posPersonajeY = 256
posPersonajeX = 70
imagenPersonaje = pygame.image.load(Path(__file__).absolute().parent / "assets/redbird-midflap.png")
personajeRect = imagenPersonaje.get_rect(center = (70,256))

#Terreno:
imagenTerreno = pygame.image.load(Path(__file__).absolute().parent / "assets/base.png")
posTerrenoX = 0
posTerrenoY = 512 - 112

velocidadJuego = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Muchas gracias")
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocidadPersonajeY = -3

    screen.blit(imagenDeFondo, (0,0))

    #Dibujar personaje:
    velocidadPersonajeY += gravedad
    personajeRect.centery += velocidadPersonajeY
    screen.blit(imagenPersonaje, personajeRect)

    posTerrenoX -= velocidadJuego
    screen.blit(imagenTerreno, (posTerrenoX, posTerrenoY))
    screen.blit(imagenTerreno, (posTerrenoX+336, posTerrenoY))

    if posTerrenoX < -288:
        posTerrenoX = 0

    pygame.display.update()
    fps.tick(60)