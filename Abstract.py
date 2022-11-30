from abc import ABC, abstractmethod

class Shape(ABC):
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printXY(self):
        print('(' + str(self.x) + ';' + str(self.y) + ')')

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    x = 0
    def __init__(self, x, y, r):
       Shape. __init__(self, x, y)
       self.r = r
    def draw(self):
        print("Draw a Circle (", self.x, ';', self.y, ';', self.r, ')', sep='')

class Rectangle(Shape):
    w = 0
    h = 0
    def __init__(self, x, y, w, h):
       Shape. __init__(self, x, y)
       self.w = w
       self.h = h
    def draw(self):
        print("Draw a Rectangle (", self.x, ';', self.y, ';', self.w, ';', self.h, ')', sep='')

c = Circle (10, 20, 5)
c.draw()

r = Rectangle(0, 0, 30, 50)
r.x = 35
r.draw()

c.printXY()
r.printXY()