from Robot import Robot
import sys, pygame
class Robots(Robot):
    #Inicializamos el arreglo de destionos
    def __init__(self):
        self.robots = []
        self.robot = Robot()

    #Funcuin para agregar destionos
    def add_robot(self,Robot):
        self.robots.append(Robot)
    #Funcion para obtener coordenadas
    def get_robot(self, index):
        return self.robots[index]
    #Funcion para actualizar valor del arreglo
    def set_robot(self, index, Robot):
        self.robots[index] = Robot
    #Fubncion para obtener el numero de destionos
    def get_size(self):
        return len(self.robots)
