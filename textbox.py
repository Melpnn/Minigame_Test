#update drawobject and textbox so that the textbox does not keep track of the value (ex: score)

from drawunit import drawunit
import pygame

class threedigittextbox(drawunit):
    def __init__(self,x,y,width,height,classtype,value):
        drawunit.__init__(self,x,y,width,height,classtype)       
        self.value = value
        self.dictionaryupdate() 
    def dictionaryupdate(self):
        self.valuedictionary = {
            "SingleDigit" : {
                "width" : 1/4 * self.width,
                "height" : self.height,
                "coordinates" : ((self.x + 11*self.width/16),self.y),
                "value" : self.value%10
            },
            "TenthDigit" : {
                "width" : 1/4 * self.width,
                "height" : self.height,
                "coordinates" :((self.x + 3*self.width/8),self.y),
                "value" : (self.value//10)%10
            },        
            "HundredthDigit" : {
                "width" : 1/4 * self.width,
                "height" : self.height,
                "coordinates" : ((self.x + self.width/16),self.y),
                "value" : (self.value//100)%10
            }                        
        }
    def drawobject(self,screen,pictures):
        screen.blit(pygame.transform.scale(pictures[str(self.valuedictionary["HundredthDigit"]["value"])]["surface"],
                                           (self.valuedictionary["HundredthDigit"]["width"],self.valuedictionary["HundredthDigit"]["height"])),
                    self.valuedictionary["HundredthDigit"]["coordinates"])
        screen.blit(pygame.transform.scale(pictures[str(self.valuedictionary["TenthDigit"]["value"])]["surface"],
                                           (self.valuedictionary["TenthDigit"]["width"],self.valuedictionary["TenthDigit"]["height"])),
                    self.valuedictionary["TenthDigit"]["coordinates"])
        screen.blit(pygame.transform.scale(pictures[str(self.valuedictionary["SingleDigit"]["value"])]["surface"],
                                           (self.valuedictionary["SingleDigit"]["width"],self.valuedictionary["SingleDigit"]["height"])),
                    self.valuedictionary["SingleDigit"]["coordinates"])
        
    def frameupdate(self,value):
        self.value = value
        self.dictionaryupdate()
