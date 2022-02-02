import pygame
import sys
from pathlib import Path

pygame.init()

screen = pygame.display.set_mode((288,512))
fps = pygame.time.Clock()
imagenDeFondo = pygame.image.load(Path(__file__).absolute().parent / "assets/background-day.png")

#Personaje:
#la "velocidad" a la que esta cayendo el personaje en un instante
velocidadPersonajeY = 0
#Posiciones del personaje
posPersonajeY = 256
posPersonajeX = 70

#Imagen del Personaje
imagenPersonaje = pygame.image.load(Path(__file__).absolute().parent / "assets/redbird-midflap.png")

#Abstrae el rect de un personaje teniendo como punto de referencia su centro, que estará ubicado en la posicion (70,256).
# Esto se puede leer como que el rect es un marco para una pintura. La pintura(imagenPersonaje) necesita estar en un cuadro. 
# Y este cuadro tiene propiedades, como una pocision que depende de su punto de referencia, en este caso centro. 
# Puede ser bottomCenter(el centro del lado Inferior) como un ejemplo. 
# el principal uso de este es el poder detectar colisiones con otros rect
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

    screen.blit(imagenDeFondo, (0,0))

    #Dibujar personaje:
    screen.blit(imagenPersonaje, personajeRect)

    posTerrenoX -= velocidadJuego
    screen.blit(imagenTerreno, (posTerrenoX, posTerrenoY))
    screen.blit(imagenTerreno, (posTerrenoX+336, posTerrenoY))

    if posTerrenoX < -288:
        posTerrenoX = 0

    pygame.display.update()
    fps.tick(60)