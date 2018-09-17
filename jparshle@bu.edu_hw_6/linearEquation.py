import math

class LinearEquation():
    """ 

    RegularPolygon class

        :params :   a       - Float - a coefficient
                :   b       - Float - b coefficient
                :   c       - Float - c coefficient 
                :   d       - Float - d coefficient 
                :   e       - Float - e coefficient 
                :   f       - Float - f coefficient 

        :returns:   linearEquation object

    """
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f       

    def __str__(self):
        s_a = str(self.__a)
        s_b = str(self.__b)
        s_c = str(self.__c)
        s_d = str(self.__d)
        s_e = str(self.__e)
        s_f = str(self.__f)
        
        returnStr = "LinearEquation a = {0}, b = {0},"\
        " c = {0}, d = {0}, e = {0}, f = {0}"

        return returnStr.format(s_a, s_b, s_c, s_d, s_e, s_f )

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def isSolvable(self):
        """ is equation solvable - Boolean """
        # create local variables to hold coefficients
        a = self.getA()
        b = self.getB()
        c = self.getC()
        d = self.getD()

        # return boolean
        return ( a * d ) - ( b * c ) != 0

    def getX(self):
        """ Solve for x - Float """
        # create local variables to hold coefficients
        a = self.getA()
        b = self.getB()
        c = self.getC()
        d = self.getD()
        e = self.getE()
        f = self.getF()

        # return x
        return ( ( e * d ) - ( b * f ) ) / ( ( a * d ) - ( b * c ) )
       
    def getY(self):
        """ Solve for y - Float """
        # create local variables to hold coefficients
        a = self.getA()
        b = self.getB()
        c = self.getC()
        d = self.getD()
        e = self.getE()
        f = self.getF()

        # return y
        return ( ( a * f ) - ( e * c ) ) / ( ( a * d ) - ( b * c ) )
       

