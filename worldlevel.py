class worldlevel():
    def __init__ (self,entitylist,timerlist,background):
        self.entitylist = entitylist
        self.timerlist = timerlist
        self.counterlist = [0] * len(entitylist)
        self.background = background
        self.backgroundx = 0
        self.background2x = 600
        self.backgroundtimer = 0
    def frameupdate(self):
        if self.backgroundtimer > 2:
            self.backgroundx-=1
            self.background2x-=1
            if self.backgroundx < -600:
                self.backgroundx=600 
            elif self.background2x < -600:
                self.background2x=600
            self.backgroundtimer=0

        self.backgroundtimer += 1
    def drawobject(self,screen):
        screen.blit(self.background,(self.backgroundx,0))
        screen.blit(self.background,(self.background2x,0))
    #def spawnobject(self):
        #for x in range (len(self.entitylist)):
