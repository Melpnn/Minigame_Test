from drawunit import drawunit
import random

class spiderenemy(drawunit):
    def __init__(self,x,y,width,height,classtype,experience):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.iframe = 0
        self.groundlevel = self.y
        self.speed = random.randint(2,4)
        self.health = 1
        self.jumpstate = False
        self.jumpframe = 0
        self.attacker = ""
        self.experience = experience
    def gethealth(self):
        return self.health
    def losehealth(self, damage, classtype):
        if self.iframe == 0:
            self.health = self.health - damage
            self.iframe = 30
            self.attacker = classtype
    def outofhealth(self):
        if self.health <= 0:
            return True
        else:
            return False
    def startjump(self):
        if not(self.jumpstate):
            self.jumpstate = True
            self.jumpframe = 0
    def getjumpheight(self):
        return (1/40)*(self.jumpframe)*(self.jumpframe - 120)
    def getiframe(self):
        return self.iframe
    def frameupdate(self):
        self.x -= self.speed
        if random.randint(1,100) == 1:
            self.startjump() 
        if self.iframe > 0:
            self.iframe -= 1
        if self.jumpstate:
            height = self.getjumpheight()
            self.y = height + self.groundlevel
            self.jumpframe += 1
            if self.jumpframe >= 120:
                self.y = self.groundlevel
                self.jumpstate = False
                self.jumpframe = 0