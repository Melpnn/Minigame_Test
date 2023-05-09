class drawunit:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def getx(self):
        return self.x
    def getrightx(self):
        return self.x + self.width
    def getbottomy(self):
        return self.y + self.height
    def gety(self):
        return self.y
    def getwidth(self):
        return self.width
    def getheight(self):
        return self.height
    def getposition(self):
        return (self.x,self.y)
    def getobjectbody(self):
        return (self.x,self.y,self.width,self.height)
    def changex(self,amount):
        self.x = self.x+amount
    def changey(self,amount):
        self.y = self.y+amount
    def checkcollision(self,objectbody):
        objectrightx = objectbody[0] + objectbody[2] 
        if self.x < objectbody[0] and self.getrightx() > objectbody[0]:
            return True and self.ycollision(objectbody)
        elif objectbody[0] < self.x and objectrightx > self.getrightx():
            return True and self.ycollision(objectbody)
        elif objectrightx > self.x and objectrightx < self.getrightx():
            return True and self.ycollision(objectbody)
        else:
            return False
    def ycollision(self,objectbody):
        objectbottomedge = objectbody[1] + objectbody[3]
        if self.y > objectbottomedge:
            return False
        elif self.getbottomy() < objectbody[1]:
            return False
        else:
            return True
        