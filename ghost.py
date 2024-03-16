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
        self.lockedstate = False 
        self.lockframe = 0
        self.blinking = False
        self.blinkframe = 0
        for columns in range(12):
            self.lasercoordinateslist.append((636*columns,0,636,145))
    def gethealthpercentage(self):
        return self.health / self.maxhealth
    def attackposition(self):
        if self.y == 200 and random.randint(1,1) == 1 and not(self.lockedstate) and self.gethealthpercentage() < 0.9:
            self.blinking = True
            self.lockedstate = True
            self.lockframe = 0
            self.blinkframe = 0
            return True
        else:
            return False
    def frameupdate(self,objectrenderlist,channel,music):
        combatant.frameupdate(self)
        self.attackposition()
        if self.blinking:
            self.blinkframe += 1
            if self.blinkframe >= 60:
                self.blinking = False
                self.blinkframe = 0
                laserbeam = laserbeamenemy(self.x - 600,self.y - 30,636,145,"enemylaserbeam_spritesheet",0,9999,self.lasercoordinateslist)
                objectrenderlist.append(laserbeam)                   
                channel.play(music["laserbeam_sfx"],2000) 
        if self.lockedstate:
            self.lockframe += 1
            if self.lockframe >= 120:
                self.lockedstate = False
                self.lockframe = 0    
                self.y += self.steps
        else:
            self.y += self.steps
            if random.randint(0,60) == 1:
                wisp = snakeenemy(self.x,self.y,20,20,"enemywisp",1,"wisp",0)
                objectrenderlist.append(wisp)
        if self.y <= 100:
            self.steps = 1
        if self.y >= 200:
            self.steps = -1
        