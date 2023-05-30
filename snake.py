from drawunit import drawunit

class snakeenemy(drawunit):
    def __init__(self,x,y,width,height,classtype,health,):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.health = health
    def gethealth(self):
        return self.health
    def losehealth(self):
        self.health = self.health - 1
    def outofhealth(self):
        if self.health <= 0:
            return True
        else:
            return False
    def frameupdate(self):
        self.changex(-1)