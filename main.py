import sys, pygame
import random
from Robot import Robot
from Robots import Robots

#Colores
black = (0,0,0)
white = (200,200,200)
red = (200,0,0)
#Inicializamos pygame
pygame.init()
size = width, height =500,500
sizeBackGrounbd = (1600,1000)
#Creamos una nueva ventana
screen = pygame.display.set_mode(size)
#Cambiamos el titulo de la ventana
pygame.display.set_caption("Robots")

#bots
x1 = width/2 - 50
y1 = height/2
tam = 25
x2 = width/2 + 50
y2 = height/2
vel = 0

#Inicializamos el sonido de fondo
#pygame.mixer.music.load("resources/img/mapa.png")

#Cambiamos el fondo de la ventana
#backGround = pygame.image.load("resources/img/mapa.png")
#backGround = pygame.transform.scale(backGround,sizeBackGrounbd)

#Funcion para pintar ciculos
robots = Robots()

def newRobots(x,y):
    robot = Robot()
    robot.set_x(x)
    robot.set_y(y)
    robots.add_robot(robot)

def drawRobots():
    if robots.get_size()>0:
        for i in range(0,robots.get_size()):

            robots.get_robot(i).set_x(robots.get_robot(i).get_x()-random.randint(-2,2))
            robots.get_robot(i).set_y(robots.get_robot(i).get_y()-random.randint(-2,2))
            pygame.draw.rect(screen,black,(robots.get_robot(i).get_pos(),(tam,tam)))
            print(robots.get_robot(i).get_pos())

#Comenzamos el bucle del jeuego
while True:
    #For para capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                vel = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            #si se presiono el boton izquierdo del mouse
            if event.button == 1:
                #obtiene la posicion del mouse dobde se presiono
                x,y=pygame.mouse.get_pos()
                newRobots(x,y)


    screen.fill(white)
    drawRobots()
    pygame.display.update()
    pygame.display.flip()
    pygame.time.delay(10)
#Salgo de pygame
pygame.quit()
