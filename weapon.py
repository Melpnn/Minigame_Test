from drawunit import drawunit
from arrows import arrows

class weapon(drawunit):
    def __init__(self,x,y,width,height,classtype):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.swingstate = False
        self.swingframe = 0
        self.weaponoffsetx = 60
        self.weaponoffsety = -30
        self.weapontype = "swordpic"
    def setswingstate(self):
        self.swingstate=True
    def getswingstate(self):
        return self.swingstate
    def getweapontype(self):
        return self.weapontype
    def toggleweapon(self):
        if self.swingstate:
            return None
        sword = "swordpic"
        bow = "bowpic"
        if self.weapontype == sword:
            self.weapontype = bow 
        else:
            self.weapontype = sword
    def frameupdate(self,slimeposition,arrowslist):
        self.x = slimeposition[0] + self.weaponoffsetx
        self.y = slimeposition[1] + self.weaponoffsety
        if self.weapontype == "swordpic" and self.swingstate:
            self.weaponoffsetx += 0.33
            self.weaponoffsety -= 0.166
            if self.weaponoffsetx >= 70:
                self.weaponoffsetx = 60
                self.weaponoffsety = -30
                self.swingstate = False
        if self.weapontype == "bowpic" and self.swingstate:
            self.weaponoffsetx -= 0.33
            if self.weaponoffsetx <= 50:
                self.weaponoffsetx = 60
                self.swingstate = False
                arrow=arrows(self.x,self.y,50,50,"arrow")
                arrowslist.append(arrow)
            