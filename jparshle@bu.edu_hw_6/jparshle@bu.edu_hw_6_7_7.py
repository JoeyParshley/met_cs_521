"""
   Joey Parshley
   MET CS 521 O2
   17 APR 2018
   hw_6_7_7
   Description: Design a class named LinearEquation for a 2 × 2 system of 
                linear equations:

                    ax+by=e     x=(ed−bf)/(ad−bc) 
                    cx+dy=f     y=(af−ec)/(ad−bc)

                The class contains:
                :   The private data fields a , b , c , d , e , and f with get 
                    methods.
                :   A constructor with the arguments for a , b , c , d , e , 
                    and f .
                :   Six get methods for a , b , c , d , e , and f .
                :   A method named isSolvable() that returns true if ad − bc 
                    is not 0 .
                :   The methods getX() and getY() that return the solution for 
                    the equation.

"""
import sys
from linearEquation import LinearEquation
N = 6

def getCoefficients():
    """
    Description: Gets the coefficients of the linear equation
        :input : coeffients - String - input from input call to user
        :return : numbers - List - List of numbers entered by the user
    """

    # ask and read numbers for the linear equation coeffients
    coefficients = (input("Enter {} numbers separated by a comma: ".format(N)))

    # split the coefficients and convert into numbers
    numbers = []
    coefficients = coefficients.split(',')
    msg = "{} is not a number please try again."

    for i  in coefficients:
        #convert coefficient to a float
        try:
            numbers.append(float(i))
        except:
            numbers.append(-1)
            print(msg.format(i))

    # make sure there are 6 coefficients
    if len(numbers) != N:
        msg = "There are not {} coefficients."
        print(msg.format(N))
        sys.exit()

    return numbers

def displaySolution(numbers):
    '''
    Description:    Displays the x and y solutions to the linear equation or the 
                    string "The equaion has no solution"
        :input :    numbers - List - numbers entered by user
        :return :   None: displays:
                        String - The solution for x and y or 
                        String - "The equation has no solution."
    '''
    a,b,c,d,e,f = numbers

    # instantiate a linearEquation object
    linearEquation1 = LinearEquation(a,b,c,d,e,f)

    if linearEquation1.isSolvable():
        print("x is {0} and y is {1}"
            .format(
                linearEquation1.getX(),
                linearEquation1.getY()
                )
            )
    else:
        print("The equation has no solution.")
 
if __name__ == '__main__':
    displaySolution(getCoefficients())
