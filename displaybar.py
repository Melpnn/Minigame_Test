from drawunit import drawunit
from pygame import transform
from pygame import Surface


class displaybar(drawunit): 
    def __init__(self,x,y,width,height,classtype,color):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.bar = Surface((width,height))
        self.bar.fill(color)
    def drawobject(self,screen,pictures,percent):
        screen.blit(transform.scale(pictures["expbar"]["surface"],(self.width,self.height)),(self.x,self.y))
        screen.blit(transform.scale(self.bar,(self.width*percent,self.height)),(self.x,self.y))

    

