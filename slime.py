from drawunit import drawunit

class slime(drawunit):
    def __init__(self,x,y,width,height,classtype,health):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.health = health
        self.jumpstate = False
        self.jumpframe = 0
        self.iframe = 0
        self.jumppower = 0.5
        self.powerupstatetimer = 0
        self.score = 0
    def gethealth(self):
        return self.health
    def getscore(self):
        return self.score
    def getiframe(self):
        return self.iframe
    def getjumpstate(self):
        return self.jumpstate
    def losehealth(self):
        self.health = self.health - 1
        self.iframe = 120
    def startjump(self):
        self.jumpstate = True
        self.jumpframe = 0
    def setjumppower(self):
        self.powerupstatetimer = 180
    def frameupdate(self):
        if self.powerupstatetimer > 0:
            self.powerupstatetimer -= 1

        if self.iframe > 0:
            self.iframe = self.iframe - 1
        if self.jumpstate:
            if self.jumpframe < 60:
                self.y -= self.jumppower
                self.jumpframe += 1
            elif self.jumpframe < 120:
                self.y += self.jumppower
                self.jumpframe += 1
            else:
                self.jumpstate = False
                self.jumpframe = 0
        else:
            if self.powerupstatetimer == 0:
                self.jumppower = 0.5
            if self.powerupstatetimer > 0:
                self.jumppower = 3