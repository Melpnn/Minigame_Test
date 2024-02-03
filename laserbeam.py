from combatants import combatant

class laserbeamenemy(combatant):
    def __init__(self,x,y,width,height,classtype,experience,health,coordinateslist):
        combatant.__init__(self,x,y,width,height,classtype,experience,health,0,2) 
        self.coordinateslist = coordinateslist
        self.animationstate = 0
        self.idleframes = 0
    def getcoordinates(self):
        if self.animationstate < 10:
            return self.coordinateslist[self.animationstate]   
        else:
            return self.coordinateslist[9]
    def outofhealth(self):
        if self.animationstate > 9:
            return True
        else:
            return False
    def frameupdate(self):
        self.idleframes+=1
        if self.idleframes >= 6:
            self.animationstate+=1
            self.idleframes=0 