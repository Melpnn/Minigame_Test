from drawunit import drawunit
import random
import math

class meteors(drawunit):
    def __init__(self,x,y,width,height,classtype):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.angle = random.randint(240,300)
        self.speed = 1
    def frameupdate(self):
        self.speed += 1/60 * self.speed
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * -1 * math.sin(math.radians(self.angle))