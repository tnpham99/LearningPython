#Question: https://ww2.cs.fsu.edu/~dennis/teaching/2017_fall_cop3330/assignments/p1/assign1.pdf

import math

class House():
    def __init__(self, base, border = 'X', fill = '*'):
        if base < 3:
            base = 3
        elif base > 37:
            base = 37
        self.__base = base
        self.__roofheight = self.__base + 2
        self.set_border(border)
        self.set_fill(fill)
    
    def get_size(self):
        return int(self.__base)

    def get_perimeter(self):
        p = self.__base * 3 + self.__roofheight * 2 + 2
        return p

    def get_area(self):
        a_roof = self.__roofheight * math.sqrt(3)/4
        a_base = self.__base**2
        a = a_roof + a_base
        return round(a,2)

    def set_border(self, border):
        if ord(border) not in range(33,127):
            self.__border = 'X'
        self.__border = border

    def set_fill(self, fill):
        if ord(fill) not in range(33,127):
            self.__fill = '*'
        self.__fill = fill

    def grow(self):
        self.__base += 1
        if self.__base > 37:
            self.__base = 37
        self.__roofheight = self.__base + 2

    def shrink(self):
        self.__base -= 1
        if self.__base < 3:
            self.__base = 3
        self.__roofheight = self.__base + 2

    def draw(self):
        print(' '*(self.__roofheight-1) + self.__border)
        roof_body = self.__roofheight - 2
        for i in range(roof_body):
            print(' '*roof_body + self.__border + (' ' + self.__fill)*i + ' ' + self.__border)
            roof_body -= 1
        print(self.__border + ' ' + self.__border + (' ' + self.__fill)*(self.__base-2) + (' ' + self.__border)*2)
        for i in range(self.__base-2):
            print(' '*2 + self.__border + (' ' + self.__fill)*(self.__base-2) + ' ' + self.__border)
        print(' '*2 + (self.__border + ' ')*self.__base)

    def summary(self):
        print(f'Base size: {self.get_size()} units')
        print(f'Perimeter: {self.get_perimeter()} units')
        print(f'Area: {self.get_area()} square units')
        self.draw()

# house1 = House(5)
# house1.summary()