from drawunit import drawunit
import random

class dragonenemy(drawunit):
    def __init__(self,x,y,width,height,classtype):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.iframe = 0
        self.speed = random.randint(2,4)
    def getiframe(self):
        return self.iframe
    def frameupdate(self):
        self.x -= self.speed
        if self.iframe > 0:
            self.iframe -= 1