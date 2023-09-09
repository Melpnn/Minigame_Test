from drawunit import drawunit

class snakeenemy(drawunit):
    def __init__(self,x,y,width,height,classtype,health,snaketype):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.health = health
        self.snaketype = snaketype
        self.iframe = 0
        self.attacker = ""
    def getsnaketype(self):
        return self.snaketype
    def gethealth(self):
        return self.health
    def getiframe(self):
        return self.iframe
    def losehealth(self,damage,classtype):
        if self.iframe == 0:
            self.health = self.health - damage
            self.iframe = 30
            self.attacker = classtype

    def outofhealth(self):
        if self.health <= 0:
            return True
        else:
            return False
    def frameupdate(self):
        self.changex(-1)
        if self.iframe > 0:
            self.iframe -= 1