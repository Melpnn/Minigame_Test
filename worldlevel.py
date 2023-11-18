from random import randint

class worldlevel():
    def __init__ (self,entitylist,timerlist,background):
        self.entitylist = entitylist
        self.timerlist = timerlist
        self.spawntimerlist = []
        for timer in timerlist:
            self.spawntimerlist.append(randint(timer[0],timer[1]))
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
        returnlist = []
        for counterindex in range (len(self.counterlist)):
            self.counterlist[counterindex]+=1
            if self.counterlist[counterindex] >= self.spawntimerlist[counterindex] and self.spawntimerlist[counterindex] != -1:
                self.counterlist[counterindex] = 0
                randmin = self.timerlist[counterindex][0]
                randmax = self.timerlist[counterindex][1]
                self.spawntimerlist[counterindex] = randint(randmin,randmax)
                returnlist.append(self.entitylist[counterindex])
        self.backgroundtimer += 1
        return returnlist
    def drawobject(self,screen):
        screen.blit(self.background,(self.backgroundx,0))
        screen.blit(self.background,(self.background2x,0))
    

    
    #def spawnobject(self):
        #for x in range (len(self.entitylist)):
