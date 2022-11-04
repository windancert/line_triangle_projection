import math
from random import random

class MyColor:
    def __init__(self, r=-1,g=-1,b=-1):
        if r == -1:
            r = 255*random()
            g = 255*random()
            b = 255*random()

        if g == -1:
            g = r
            b = r
        self.r = self._check_color(r)
        self.g = self._check_color(g)
        self.b = self._check_color(b)

    def _check_color(self,c):
        c = int(math.floor(c))
        if c < 0 : 
            c = 0
        elif c > 255 : 
            c = 255
        return c

    def __str__(self):
        str = f"#{self.r:02X}{self.g:02X}{self.b:02X}"
        return str



# autotesters
if __name__ == '__main__':
    print("simple input")
    c = my_color(1,2,3)
    print(str(c))
    print("single input")
    c = my_color(255)
    print(str(c))
    print("(too)large input")
    c = my_color(77,200,300)
    print(str(c))
    print("negative and decimal")
    c = my_color(-1,2.7,300)
    print(str(c))
    print("random")
    c = my_color()
    print(str(c))
