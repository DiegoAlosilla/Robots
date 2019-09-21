import random
class Obstacle():
    x=y=0
    color = [0,0,0]

    #---------------GET---------------
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

    #---------------SET---------------
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y

    #---------------------------------
    def get_pos(self):
        return (self.x,self.y)

    def collisionObject(self,x,y):
        if self.x + 25 > x and self.x  < x +25 and self.y + 25 > y and self.y < y + 25:
            self.speedY = ranadom.randint(0,500-25)
            self.speedX = ranadom.randint(0,500-25)
