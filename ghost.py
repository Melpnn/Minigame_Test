from combatants import combatant
from snake import snakeenemy
from laserbeam import laserbeamenemy
import random

class ghostenemy(combatant):
    def __init__(self,x,y,width,height,classtype,experience,health,speed,atkpower):
        combatant.__init__(self,x,y,width,height,classtype,experience,health,speed,atkpower)     
        self.steps = -1
        self.maxhealth = 20
        self.lasercoordinateslist = []
        for columns in range(12):
            self.lasercoordinateslist.append((318*columns,0,318,145))
    def gethealthpercentage(self):
        return self.health / self.maxhealth
    def attackposition(self):
        if self.y == 150 and random.randint(1,1) == 1:
            return True
        else:
            return False
    def frameupdate(self,objectrenderlist):
        combatant.frameupdate(self)
        self.y += self.steps
        if self.y <= 100:
            self.steps = 1
        if self.y >= 200:
            self.steps = -1
        if random.randint(0,60) == 1:
            wisp = snakeenemy(self.x,self.y,20,20,"enemywisp",1,"wisp",0)
            objectrenderlist.append(wisp)
        if self.gethealthpercentage() < 0.99 and self.attackposition():  
            laserbeam = laserbeamenemy(self.x,self.y,318,145,"enemylaserbeam_spritesheet",0,9999,self.lasercoordinateslist)
            objectrenderlist.append(laserbeam)        
        