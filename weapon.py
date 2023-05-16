from drawunit import drawunit
from arrows import arrows

class weapon(drawunit):
    def __init__(self,x,y,width,height,classtype):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.swingstate = False
        self.swingframe = 0
        self.swordoffsetx = 60
        self.swordoffsety = -30
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
        self.x = slimeposition[0] + self.swordoffsetx
        self.y = slimeposition[1] + self.swordoffsety
        if self.weapontype == "swordpic" and self.swingstate:
            self.swordoffsetx += 0.33
            self.swordoffsety -= 0.166
            if self.swordoffsetx >= 70:
                self.swordoffsetx = 60
                self.swordoffsety = -30
                self.swingstate = False
        if self.weapontype == "bowpic" and self.swingstate:
            self.swordoffsetx -= 0.33
            if self.swordoffsetx <= 50:
                self.swordoffsetx = 60
                self.swingstate = False
                arrow=arrows(self.x,self.y,50,50,"arrow")
                arrowslist.append(arrow)