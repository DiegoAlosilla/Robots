from Obstacle import Obstacle
import sys, pygame,random

class Obstacles(Obstacle):
    #Inicializamos el arreglo de destionos
    def __init__(self):
        self.obstacles = []

        for i in range(0,10):
            self.obstacle = Obstacle()
            self.obstacle.set_x(random.randint(0,500))
            self.obstacle.set_y(random.randint(0,500))
            self.add_obstacle(self.obstacle)

    #Funcuin para agregar destionos
    def add_obstacle(self,Obstacle):
        self.obstacles.append(Obstacle)
    #Funcion para obtener coordenadas
    def get_obstacle(self, index):
        return self.obstacles[index]
    #Funcion para actualizar valor del arreglo
    def set_obstacle(self, index, Obstacle):
        self.obstacles[index] = Obstacle
    #Fubncion para obtener el numero de destionos
    def get_size(self):
        return len(self.obstacles)
