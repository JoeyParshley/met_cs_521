from GeometricObject import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self, w = 1, h = 1):
        super.__init__()
        self.__width = w
        self.__height = h

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self.height):
        self.__height = height

    def get_area(self):
        return self.__height * self.__width

    def get_perimeter(self):
        return 2 * (self.__height + self.__width)
