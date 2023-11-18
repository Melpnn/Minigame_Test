from drawunit import drawunit
from snake import snakeenemy
import random

class ghostenemy(drawunit):
    def __init__(self,x,y,width,height,classtype,experience):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.iframe = 0
        self.steps = -1
        self.health = 1
        self.attacker = ""
        self.experience = experience
    def frameupdate(self,objectrenderlist):
        self.y += self.steps
        if self.y <= 100:
            self.steps = 1
        if self.y >= 200:
            self.steps = -1
        if random.randint(0,60) == 1:
            wisp = snakeenemy(self.x,self.y,20,20,"coin",1,"wisp",0)
            objectrenderlist.append(wisp)

        
        