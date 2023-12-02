from combatants import combatant
from snake import snakeenemy
import random

class ghostenemy(combatant):
    def __init__(self,x,y,width,height,classtype,experience,health,speed,atkpower):
        combatant.__init__(self,x,y,width,height,classtype,experience,health,speed,atkpower)     
        self.steps = -1
        self.maxhealth = 20
    def gethealthpercentage(self):
        return self.health / self.maxhealth
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

        
        