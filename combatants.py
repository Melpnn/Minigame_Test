from drawunit import drawunit

class combatant(drawunit):
    def __init__(self,x,y,width,height,classtype,experience,health,speed,atkpower):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.iframe = 0
        self.attacker = ""
        self.experience = experience
        self.health = health
        self.speed = speed
        self.atkpower = atkpower
    def losehealth(self,damage,classtype):
        if self.iframe == 0:
            self.health = self.health - damage
            self.iframe = 30
            self.attacker = classtype    
    def frameupdate(self):
        if self.iframe > 0:
            self.iframe -= 1       
    def outofhealth(self):
        if self.health <= 0:
            return True
        else:
            return False