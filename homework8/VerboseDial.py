class Dial:

    def __init__(self, tot, on, off):
        self.first = '['
        self.next = 0 * str(on)
        self.then = str(off) * tot
        self.last = ']'
        self.ret = self.first + self.next + self.then + self.last
        self.oldMax = 0
        self.tot = tot
        self.on = str(on)
        self.off = str(off)
    
    def display(self):
        print(self.ret)

    def increaseBy(self,inc):
        x = inc + self.oldMax
        if x > self.tot:
            x = self.tot
        self.next = str(x * self.on)
        self.then = (self.tot - x) * str(self.off)
        self.ret = self.first + self.next + self.then + self.last
        self.oldMax = x

    def decreaseBy(self,dec):
        x = self.oldMax - dec
        if x < 0:
            x = 0
        self.next = str(x * self.on)
        self.then = (self.tot - x) * str(self.off)
        self.ret = self.first + self.next + self.then + self.last
        self.oldMax = x

class VerboseDial:

    def __init__(self, tot, on, off):
        self.first = '['
        self.next = 0 * str(on)
        self.then = str(off) * tot
        self.last = ']'
        self.ret = self.first + self.next + self.then + self.last
        self.oldMax = 0
        self.tot = tot
        self.on = str(on)
        self.off = str(off)
    
    def display(self):
        print(self.ret)

    def increaseBy(self,inc):
        x = inc + self.oldMax
        if x > self.tot:
            x = self.tot
        self.next = str(x * self.on)
        self.then = (self.tot - x) * str(self.off)
        self.ret = self.first + self.next + self.then + self.last
        self.oldMax = x
        print(self.ret)

    def decreaseBy(self,dec):
        x = self.oldMax - dec
        if x < 0:
            x = 0
        self.next = str(x * self.on)
        self.then = (self.tot - x) * str(self.off)
        self.ret = self.first + self.next + self.then + self.last
        self.oldMax = x
        print(self.ret)