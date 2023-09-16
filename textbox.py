from drawunit import drawunit

class threedigittextbox(drawunit):
    def __init__(self,x,y,width,height,classtype,transparency,value):
        drawunit.__init__(self,x,y,width,height,classtype)       
        self.transparency = transparency
        self.value = value
        self.valuedictionary = {
            "SingleDigit" : {
                "width" : 1/4 * width,
                "height" : height,
                "coordinates" : ((x + 11*width/16),y),
                "value" : value%10
            },
            "TenthDigit" : {
                "width" : 1/4 * width,
                "height" : height,
                "coordinates" :((x + 3*width/8),y),
                "value" : (value//10)%10
            },        
            "HundredthDigit" : {
                "width" : 1/4 * width,
                "height" : height,
                "coordinates" : ((x + width/16),y),
                "value" : (value//100)%10
            }            
        }