import pygame
import sys
from pathlib import Path

##Pequeña refactorización a funciones
def CrearTubo():
#Cogemos como referencia el puntoMedio de la parte superior y lo ubicamos fuera de la pantalla por el lado derecho
    tuboAbajo = imagenTubo.get_rect(midtop = (300, 200))
    return tuboAbajo

def MoverTubos(ListaDeTubos):
    for tubo in listaTubos:
        tubo.centerx -= 5
    return listaTubos

def DibujarTubos(ListaDeTubos):
    #Se Dibuja cada lista de tubos 
    for tubo in listaTubos:
        screen.blit(imagenTubo, tubo)


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

#Tubos:
imagenTubo = pygame.image.load(Path(__file__).absolute().parent / "assets/pipe-green.png")
#Crear lista vacia donde luego estarán todos los tubos
listaTubos = []

#Crear evento Custom que sucederá cada 2 segundos
CREARTUBO = pygame.USEREVENT
pygame.time.set_timer(CREARTUBO, 2000)

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
        
        if event.type == CREARTUBO:            
            listaTubos.append(CrearTubo())

    screen.blit(imagenDeFondo, (0,0))

    #Dibujar personaje:
    velocidadPersonajeY += gravedad
    personajeRect.centery += velocidadPersonajeY
    screen.blit(imagenPersonaje, personajeRect)

    
    #Mostrar tubos:
    listaTubos = MoverTubos(listaTubos)
    DibujarTubos(listaTubos)
    

    posTerrenoX -= velocidadJuego
    screen.blit(imagenTerreno, (posTerrenoX, posTerrenoY))
    screen.blit(imagenTerreno, (posTerrenoX+336, posTerrenoY))

    if posTerrenoX < -288:
        posTerrenoX = 0

    pygame.display.update()
    fps.tick(60)