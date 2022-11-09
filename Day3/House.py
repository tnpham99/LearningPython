#Question: https://ww2.cs.fsu.edu/~dennis/teaching/2017_fall_cop3330/assignments/p1/assign1.pdf

import math

class House():
    def __init__(self, base, border = 'X', fill = '*'):
        self.__base = base
        self.__border = border
        self.__fill = fill
        if base < 3:
            self.__base = 3
        if base > 37:
            self.__base = 37
        self.__roofside = self.__base + 2
        self.__SetBorder()
        self.__SetFill()
    
    def __GetSize(self):
        return f'Base size: {int(self.__base)} units'

    def __GetPerimeter(self):
        p = self.__base * 3 + self.__roofside * 2 + 2
        return f'Perimeter: {p} units'

    def __GetArea(self):
        a_roof = self.__roofside * math.sqrt(3)/4
        a_base = self.__base**2
        a = a_roof + a_base
        return f'Area: {round(float(a),2)} square units'

    def Grow(self):
        self.__base = self.__base + 1
        if self.__base > 37:
            self.__base = 37
        self.__roofside = self.__base + 2

    def Shrink(self):
        self.__base = self.__base - 1
        if self.__base < 3:
            self.__base = 3
        self.__roofside = self.__base + 2

    def __SetBorder(self):
        if ord(self.__border) not in range(33,127):
            self.__border = 'X'
        
    def __SetFill(self):
        if ord(self.__fill) not in range(33,127):
            self.__fill = '*'

    def __Draw(self):
        print(' '*(self.__roofside-1) + self.__border)
        draw_roof = self.__roofside - 2
        for i in range(draw_roof):
            print(' '*draw_roof + self.__border + (' ' + self.__fill)*i + ' ' + self.__border)
            draw_roof = draw_roof - 1
        print(self.__border + ' ' + self.__border + (' ' + self.__fill)*(self.__base-2) + (' ' + self.__border)*2)
        for i in range(self.__base-2):
            print(' '*2 + self.__border + (' ' + self.__fill)*(self.__base-2) + ' ' + self.__border)
        print(' '*2 + (self.__border + ' ')*self.__base)

    def Summary(self):
        print(self.__GetSize())
        print(self.__GetPerimeter())
        print(self.__GetArea())
        print(self.__Draw())

house1 = House(3)
house1.Summary()