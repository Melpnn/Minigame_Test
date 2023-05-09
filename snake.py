from drawunit import drawunit

class snakeenemy(drawunit):
    def __init__(self,x,y,width,height,health):
        drawunit.__init__(self,x,y,width,height)
        self.health = health
    def gethealth(self):
        return self.health
    def losehealth(self):
        self.health = self.health - 1