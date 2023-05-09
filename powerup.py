from drawunit import drawunit

class powerup(drawunit):
    def __init__(self,x,y,width,height,timer):
        drawunit.__init__(self,x,y,width,height)
        self.timer = timer
    def checktimer(self):
        self.timer = self.timer-1
        return self.timer
