from drawunit import drawunit

class powerup(drawunit):
    def __init__(self,x,y,width,height,classtype,timer):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.timer = timer
    def checktimer(self):
        return self.timer
    def frameupdate(self):
        self.timer-=1
        if self.timer <= 0:
            self.x = 650
        if self.y <= 233:
            self.changey(1)
