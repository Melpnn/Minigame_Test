from drawunit import drawunit
from arrows import arrows

class weapon(drawunit):
    def __init__(self,x,y,width,height,classtype):
        drawunit.__init__(self,x,y,width,height,classtype)
        self.swingstate = False
        self.specialstate = False
        self.attackbarcount = 0
        self.weaponoffsetx = 60
        self.weaponoffsety = -30
        self.weapontype = "swordpic"
    def setswingstate(self):
        if self.swingstate == False:
            self.swingstate = True
            return True
        else:
            return False
    def getswingstate(self):
        return self.swingstate
    def setspecialattackstate(self):
        if self.attackbarcount > 0:
            self.specialstate = True
    def getspecialattackstate(self):
        return self.specialstate
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
                arrow = arrows(self.x,self.getmiddley()-5,30,10,"arrow")
                arrowslist.append(arrow)
        elif self.weapontype == "bowpic" and self.specialstate:
            self.weaponoffsetx -= 0.33
            if self.weaponoffsetx <= 50:
                self.weaponoffsetx = 60
                self.attackbarcount -= 1
                self.specialstate = False
                arrow = arrows(self.x,self.getmiddley()-15,50,30,"bigarrow")
                arrowslist.append(arrow)
            