from drawunit import drawunit
import random

class critters(drawunit):
    def __init__(self,x,y,width,height,classtype,coordinateslist):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.coordinateslist=coordinateslist
        self.animationstate=random.randint(0,len(coordinateslist)-1)
        self.idleframes=0
    def getcoordinates(self):
        return self.coordinateslist[self.animationstate%len(self.coordinateslist)]
    def frameupdate(self):
        self.x+=1
        self.idleframes+=1
        if self.idleframes >= 15:
            self.animationstate+=1
            self.idleframes=0
        
        


