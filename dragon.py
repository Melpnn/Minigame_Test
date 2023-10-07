from drawunit import drawunit
import random

class dragonenemy(drawunit):
    def __init__(self,x,y,width,height,classtype,experience):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.iframe = 0
        self.speed = random.randint(2,4)
        self.health = 1
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
    def getiframe(self):
        return self.iframe
    def frameupdate(self):
        self.x -= self.speed
        if self.iframe > 0:
            self.iframe -= 1