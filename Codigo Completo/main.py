import pygame
import sys
import random

def CrearTubo():
    alturaRandom = random.choice(alturaTubos)
    tuboAbajo = imagenTubo.get_rect(midtop = (300,alturaRandom))
    tuboArriba = imagenTubo.get_rect(midbottom = (300,alturaRandom - 150))
    return tuboAbajo, tuboArriba

def MoverTubos(ListaDeTubos):
    for tubo in listaTubos:
        tubo.centerx -= 5
    return listaTubos

def DibujarTubos(ListaDeTubos):
    for tubo in listaTubos:
        if tubo.bottom >400:
            screen.blit(imagenTubo, tubo)
        else: 
            imagenVolteada = pygame.transform.flip(imagenTubo, False, True)
            screen.blit(imagenVolteada, tubo)


def RevisarColisiones(ListaDeTubos):
    for tubo in ListaDeTubos:
        if personajeRect.colliderect(tubo):
            return False
    if personajeRect.top < -100:
        return False
    elif personajeRect.bottom > 420:
        return False
    else:
        return True

def RevisarPuntaje():
    global puntaje
    global puedeRecibirPuntaje

    if listaTubos:
        for tubo in listaTubos:
            if 65 < tubo.centerx <75 and puedeRecibirPuntaje:
                puntaje += 1
                print(puntaje)
                puedeRecibirPuntaje = False
            if tubo.centerx < 0:
                puedeRecibirPuntaje = True

def MostrarPuntaje():
    letrasPuntaje = fuenteDePuntaje.render(str(puntaje), True, (255,255,255))
    screen.blit(letrasPuntaje,(144,30))

pygame.init()
screen = pygame.display.set_mode((288,512))
fps = pygame.time.Clock()
estadoJuego = True
fuenteDePuntaje = pygame.font.Font("assets/04B_19.ttf",30)
puntaje = 0
puedeRecibirPuntaje = True


#GameOver:
imagenGameOver = pygame.image.load("assets/gameover.png") 
gameOverRect = imagenGameOver.get_rect(center = (144,256))

imagenDeFondo = pygame.image.load("assets/background-day.png")
posImagen = 0
#Variables del terreno:
terreno = pygame.image.load("assets/base.png")
posTerrenoY = 512-112
posTerrenoX = 0

#Personaje:
gravedad = 0.1
posPersonajeY = 0
personaje = pygame.image.load("assets/redbird-midflap.png")
personajeRect = personaje.get_rect(center = (70,256))

#Tubos:
imagenTubo = pygame.image.load("assets/pipe-green.png")
listaTubos = []
CREARTUBO = pygame.USEREVENT
pygame.time.set_timer(CREARTUBO, 2000)
alturaTubos = [250, 200, 180, 225, 190]

while True:
    #Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if estadoJuego:
                    posPersonajeY = 0
                    posPersonajeY -= 3
                else:
                    #Reiniciar juego:
                    estadoJuego = True
                    listaTubos.clear()
                    personajeRect.center = (70,256)
                    posPersonajeY = 0
                    puntaje = 0
        if event.type == CREARTUBO:
            listaTubos.extend(CrearTubo())

    ##Parte de la image de fondo con la animacion de movimiento
    posImagen = posImagen - 0.6
    screen.blit(imagenDeFondo,(posImagen,0))
    screen.blit(imagenDeFondo,(posImagen + 288,0))
    if posImagen < -288:
        posImagen = 0


    
    if estadoJuego:
        ##personaje
        posPersonajeY = posPersonajeY + gravedad
        personajeRect.centery = personajeRect.centery + posPersonajeY
        screen.blit(personaje,personajeRect)

        #Mostrar tubos:
        listaTubos = MoverTubos(listaTubos)
        DibujarTubos(listaTubos)

        estadoJuego = RevisarColisiones(listaTubos)
        ## animacion del terreno
        posTerrenoX = posTerrenoX - 1 
        RevisarPuntaje()
        MostrarPuntaje()
    else:
        screen.blit(imagenGameOver,gameOverRect)
    
        
    screen.blit(terreno,(posTerrenoX,posTerrenoY))
    screen.blit(terreno,(posTerrenoX+336,posTerrenoY))

    if posTerrenoX < -300:
        posTerrenoX = 0

    pygame.display.update()
    fps.tick(60)