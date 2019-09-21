import sys, pygame
import random
import os
from Robot import Robot
from Robots import Robots
from Obstacle import Obstacle
from Obstacles import Obstacles

#Colores
black = (0,0,0)
white = (200,200,200)
green  = (87,166,57)
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
tam = 25
#Inicializamos el sonido de fondo
#pygame.mixer.music.load("resources/img/mapa.png")

bg = pygame.image.load("src/SpaceShooterRedux/Backgrounds/black.png")
bg = pygame.transform.scale(bg,(width, height))

tank = pygame.image.load("src/img/src.png")
tank = pygame.transform.scale(tank,(595, 400))

meteoro = pygame.image.load("src/SpaceShooterRedux/PNG/Meteors/meteorBrown_big4.png")
meteoro = pygame.transform.scale(meteoro,(25, 25))



robots = Robots()
obstacles = Obstacles()

def newRobots(x,y):
    robot = Robot()
    robot.set_x(x)
    robot.set_y(y)
    robot.set_speedX(random.choice((-1, 1)))
    robot.set_speedY(random.choice((-1, 1)))
    robots.add_robot(robot)

def newObstacle():
    for i in range(0,20):
        osbstacle = Obstacle()
        osbstacle.set_x(ranadom.randint(0,500-25))
        osbstacle.set_y(ranadom.randint(0,500-25))
        obstacles.add_obstacle(osbstacle)

def drawObstacle():
    if obstacles.get_size()>0:
        for i in range(0,obstacles.get_size()):
            #pygame.draw.rect(screen,red,(obstacles.get_obstacle(i).get_pos(),(tam,tam)))
            screen.blit(meteoro,(obstacles.get_obstacle(i).get_pos()) )

run = True

def drawRobots():
    if robots.get_size()>0:
        for i in range(0,robots.get_size()):
            if robots.get_robot(i).get_vidas() > 0:
                for j in range(0,robots.get_size()):
                    if j != i:
                        x = robots.get_robot(j).get_x()
                        y = robots.get_robot(j).get_y()
                        robots.get_robot(i).collisionObject(x,y)
                        if robots.get_robot(i).get_vidas() ==0:
                            robots.delete_robot(i)
                        if robots.get_size() == 0:
                            pygame.quit()
                            break

                for j in range(0,obstacles.get_size()):
                    x = obstacles.get_obstacle(j).get_x()
                    y = obstacles.get_obstacle(j).get_y()
                    robots.get_robot(i).collisionObject(x,y)
                robots.get_robot(i).collisionWindows(width,height)
                robots.get_robot(i).move()
            #pygame.draw.rect(screen,black,(robots.get_robot(i).get_pos(),(tam,tam)))
                screen.blit(robots.get_robot(i).get_img(),(robots.get_robot(i).get_pos()))
                print('Robot ',i,' ',robots.get_robot(i).get_pos(),' ',robots.get_robot(i).get_vidas())



#Comenzamos el bucle del jeuego
while run:
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


    screen.blit(bg,(0,0))
    drawRobots()
    drawObstacle()
    pygame.display.update()
    pygame.display.flip()
    pygame.time.delay(10)
#Salgo de pygame
pygame.quit()
