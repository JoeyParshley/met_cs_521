import math

class RegularPolygon():
    """ 

    RegularPolygon class

        :params :   n       - Int - number of sides default - 3
                :   side    - Float - length of sides default - 1
                :   x       - Float - x coordinate of center default - 0 
                :   y       - Float - y coordinate of center default - 0 

        :returns:   account object

    """
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def __str__(self):
        s_n = str(self.__n)
        s_side = str(self.__side)
        s_x = str(self.__x)
        s_y = str(self.__y)

        returnStr = "RegularPolygon n = {0}, side = {1}, x = {2}, y = {3}"

        return returnStr.format(s_n, s_side, s_x, s_y)

    def getN(self):
        return self.__n

    def setN(self):
        self.__n = n

    def getSide(self):
        return self.__side

    def setSide(self,side):
        self.__side = side

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self ,y):
        self.__y = y

    def getPerimeter(self):
        """ Get Perimeter of Polygon based on sides """
        return self.getN() * self.getSide()

    def getArea(self):
        """ Get Area of Polygon based on sides """
        n = self.getN()
        s = self.getSide()
        return (n * s ** 2) / ( 4 * math.tan ( math.pi / n ) )


