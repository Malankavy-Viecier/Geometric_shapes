class Point:
    __x = 0
    __y = 0
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def __test(self): #private
        print("Private method")
    def runPrivate(self): #public
        self.__test()

p = Point(21,25)

print(p.getX())
print(p.getY())
p.setX(28)
p.setY(33)
print(p.getX())
print(p.getY())

p.runPrivate()
