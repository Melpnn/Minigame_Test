from drawunit import drawunit

class slime(drawunit):
    def __init__(self,x,y,width,height,classtype,health):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.groundlevel = self.y
        self.health = health
        self.healthcap = 5
        self.jumpstate = False
        self.jumpframe = 0
        self.iframe = 0
        self.powerupstatetimer = 0
        self.score = 0
        self.attacker = ""
        self.level = 0
        self.experiencecap = 25
        self.currentexperience = 0 
        self.speed = 1
    def gethealth(self):
        return self.health
    def getscore(self):
        return self.score
    def getiframe(self):
        return self.iframe
    def getjumpstate(self):
        return self.jumpstate
    def getjumpheight(self):
        return (1/20)*(self.jumpframe)*(self.jumpframe - 120)
    def offscreen(self):
        if self.getrightx() > 600 or self.x < 0:
            return True
        else:
            return False    
    def getexppercent(self):
        return self.currentexperience/self.experiencecap
    def updateexperience(self,expgain):
        self.currentexperience += expgain  
        if self.currentexperience >= self.experiencecap:
            self.level += 1
            self.experiencecap += 50
            self.currentexperience = 0
            if self.speed <= 3:
                self.speed += 0.5
    def restorehealth(self):
        if self.health < self.healthcap:
            self.health +=1
    def losehealth(self,damage,classtype):
        if self.getiframe() == 0:
            self.health = self.health - damage
            self.iframe = 120
            self.attacker = classtype
    def startjump(self):
        self.jumpstate = True
        self.jumpframe = 0
    def setjumppower(self):
        return None
    def frameupdate(self):
        if self.powerupstatetimer > 0:
            self.powerupstatetimer -= 1

        if self.iframe > 0:
            self.iframe = self.iframe - 1
        if self.jumpstate:
            height = self.getjumpheight()
            self.y = height + self.groundlevel
            self.jumpframe += 1
            if self.jumpframe >= 120:
                self.y = self.groundlevel
                self.jumpstate = False
                self.jumpframe = 0