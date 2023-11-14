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
            print(False)
        else: 
            self.fuelSize -= (dist / self.mpg)
            self.x = x2
            self.y = y2
            print(True)
    
    def getLocationX(self):
        print(self.x)
    
    def getLocationY(self):
        print(self.y)

    def getGas(self):
        self.fuelSize = self.origFuelSize
    
    def getToFill(self):
        ret = self.origFuelSize - self.fuelSize
        print(ret)

class Taxi:

    def __init__(self, mpg, fuelSize):
        self.x = 0
        self.y = 0
        self.mpg = mpg
        self.fuelSize = fuelSize
        self.origFuelSize = fuelSize
        self.passenger = False
        self.distance = 0
        self.money = 0

    def driveTo(self, x2, y2):
        dist = sqrt(abs((x2 - self.x) ** 2 + (y2 - self.y) ** 2))
        if self.fuelSize < dist / self.mpg:
            return False
        else: 
            self.fuelSize -= (dist / self.mpg)
            self.x = x2
            self.y = y2
            if self.passenger == True:
                self.distance = dist
                self.money = self.money + (2 + (self.distance * 3))
            if self.passenger == False:
                self.distance = 0
            return True
    
    def getLocationX(self):
        return self.x
    
    def getLocationY(self):
        return self.y

    def getGas(self):
        return self.fuelSize
    
    def getToFill(self):
        ret = self.origFuelSize - self.fuelSize
        return ret 

    def pickup(self):
        if self.passenger == True:
            return False
        else:
            self.passenger = True
            return True
    
    def dropoff(self):
        if self.passenger == False:
            return False
        else:
            self.passenger = False
            return True
    
    def getMoney(self):
        return self.money
