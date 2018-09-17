class Rectangle():
    def __init__(self, w = 1, h = 2):
        self.__width = w
        self.__height = h

    def __str__(self):
        s_width = str(self.__width)
        s_height = str(self.__height)
        return "Rectangle w = {0}, h = {1}".format(s_width, s_height)

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_area(self):
        return self.__height * self.__width

    def get_perimeter(self):
        return 2 * (self.__height + self.__width)
