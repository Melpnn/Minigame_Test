from combatants import combatant

class snakeenemy(combatant):
    def __init__(self,x,y,width,height,classtype,health,snaketype,experience):
        combatant.__init__(self,x,y,width,height,classtype,experience,health,speed=0,atkpower=0)
        self.snaketype = snaketype
    def getsnaketype(self):
        return self.snaketype
    def gethealth(self):
        return self.health
    def getiframe(self):
        return self.iframe
    def frameupdate(self):
        self.changex(-1)
        if self.iframe > 0:
            self.iframe -= 1