from GeometricObject import GeometricObject
import math

class Triangle(GeometricObject):

    """ 

    Triangle class - subclass of GeometricObject

        :params :   side1 - Float - the length of the side1 default - 1
                :   side2 - Float - the length of the side2 default - 1
                :   side3 - Float - the length of the side3 default - 1 

        :returns: Triangle object

    """

    def __init__(self, side1 = 1, side2 = 1, side3 = 1):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def __getS(self, s1, s2, s3):
        return ( s1 + s2 + s3) / 2

    def getSide1(self):
        return self.__side1

    def setSide1(self, s1):
        self.__side1 = s1
        
    def getSide2(self):
        return self.__side2

    def setSide2(self, s2):
        self.__side2 = s2
        
    def getSide3(self):
        return self.__side3

    def setSide3(self, s3):
        self.__side3 = s3
        
    def getArea(self):
        """ Returns Area of triangle based on length of the sides """
        s1 = self.getSide1()
        s2 = self.getSide2()
        s3 = self.getSide3()
        s = self.__getS(s1, s2, s3)

        return math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

    def getPerimeter(self):
        """ Returns Perimeter of triangle """
        s1 = self.getSide1()
        s2 = self.getSide2()
        s3 = self.getSide3()
        return s1 + s2 + s3

    def __str__(self):
        return "Triangle: side1 = "  + str(self.__side1) +  \
            " side2 = "  + str(self.__side2) +  \
            " side3 = "  + str(self.__side3)
