import random
import sys, pygame
class Robot():
    def __init__(self):
        self.x=self.y=0
        self.vidas = 3
        self.speedX=self.speedY = 0
        self.tam = 25
        self.numImg = random.randint(1,20)
        self.str = 'src/SpaceShooterRedux/PNG/Enemies/'+ str(self.numImg) +'.png'
        self.img = pygame.image.load(self.str)
        self.img = pygame.transform.scale(self.img,(self.tam, self.tam))
        self.sonido = pygame.mixer.Sound("src/SpaceShooterRedux/Bonus/sfx_lose.ogg")
        self.sonido2 = pygame.mixer.Sound("src/SpaceShooterRedux/Bonus/sfx_shieldDown.ogg")
    #---------------GET---------------
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_speedX(self):
        return self.speedX
    def get_speedY(self):
        return self.speedY
    def get_color(self):
        return tuple(self.rgbl)
    def get_img(self):
        return self.img
    def get_vidas(self):
        return self.vidas

    #---------------SET---------------
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def set_speedX(self,speedX):
        self.speedX = speedX
    def set_speedY(self,speedY):
        self.speedY = speedY
    def set_color(self,rgbl):
        self.rgbl = rgbl



    def collisionObject(self,x,y):
        if self.x + 25 >= x and self.x  <= x +25 and self.y + 25 >= y and self.y <= y + 25:
            self.speedY *=-1
            self.speedX *=-1
            self.sonido.play()
            self.vidas -=1

    def collisionWindows(self,x,y):

        if self.x + 25 >= x or self.x  <= 0:
            self.speedX *=-1
            self.sonido2.play()
        if  self.y + 25 >= y or self.y <= 0:
            self.speedY *=-1
            self.sonido2.play()


    def move(self):
        self.x += self.speedX
        self.y += self.speedY

    def get_pos(self):
        return (self.x,self.y)
