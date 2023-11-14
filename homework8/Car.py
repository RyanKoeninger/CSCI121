from math import *

class Car:

    def __init__(self, mpg, fuelSize):
        self.x = 0
        self.y = 0
        self.mpg = mpg
        self.fuelSize = fuelSize
        self.origFuelSize = fuelSize

    def driveTo(self, x2, y2):
        dist = sqrt(abs((x2 - self.x) ** 2 + (y2 - self.y) ** 2))
        if self.fuelSize < dist / self.mpg:
            return False
        else: 
            self.fuelSize -= (dist / self.mpg)
            self.x = x2
            self.y = y2
            return True
    
    def getLocationX(self):
        return(self.x)
    
    def getLocationY(self):
        return(self.y)

    def getGas(self):
        return self.fuelSize
    
    def getToFill(self):
        ret = self.origFuelSize - self.fuelSize
        return(ret)
