"""
   Joey Parshley
   MET CS 521 O2
   17 APR 2018
   hw_6_12_1
   Description: Design a class named Triangle that extends the GeometricObject 
                class. The Triangle class contains:
                :   Three float data fields named side1 , side2 , and side3 to 
                    denote the three sides of the triangle.
                :   A constructor that creates a triangle with the specified 
                    side1 , side2 , and side3 with default values 1.0 .
                :   The accessor methods for all three data fields.
                :   A method named getArea() that returns the area of this 
                    triangle.
                :   A method named getPerimeter() that returns the perimeter 
                    of this triangle.
                :   A method named __str__() that returns a string description 
                    for the triangle.

                    For the formula to compute the area of a triangle,
                    The __str__() method is implemented as follows:

            return  "Triangle: side1 = "  + str(side1) +  " side2 = "  + 
            str(side2) +  " side3 = "  + str(side3)


            Implement the Triangle class. Write a test program that prompts the 
            user to enter the three sides of the triangle, a color, and 1 or 0 
            to indicate whether the triangle is filled. The program should 
            create a Triangle object with these sides and set the color and 
            filled properties using the input. The program should display the 
            triangle’s area, perimeter, color, and True or False to indicate 
            whether the triangle is filled or not.

"""
import sys
from triangle import Triangle
N = 3

def getTriangleProperties():
    """
    Description: Gets the lengths of the sides of the triangle
        :input : side - String - input from input call to user
        :return : lengths - List - List of numbers lengths entered by the user
    """

    # ask and read the three sides
    sides = ( input ( "Enter the {} lengths for the sides of a triangle: "
        .format(N)))
    
    # split the read string of numbers into a list numbers
    props = []
    sides = sides.split(',')
    msg = "{} is not a numbe please try again."

    for s in sides:
        # convert side to a float
        try:
            props.append(float(s))
        except:
            props.append(-1)
            print(msg.format(N))

    # make sure that there are 3 sides
    if len(props) != N:
        msg = "There are not {} numbers."
        print(msg.format(N))
        sys.exit()
    color = input( "Enter the color of your triangle as a string. ")
    filled = getFilledBoolean(
        input( "Enter True or False is the triangle is filled. ")
        ) 

    props.append(color)
    props.append(filled)

    return props

def getFilledBoolean(str):
    """
    Description: determine is triangle should be filled
        :input : str - String - user entered value 'true' or 'false'

        :return : - Boolean
    """
    # If user does not enter true or false, exit.
    if str.lower() == 'true':
        return True
    elif str.lower() == 'false':
        return False
    else:
        print("Please enter 'True' or 'False' for the filled state.")
        sys.exit()

def getFilledString(bool):
    """
    Description : return the string for whether the traingle is filled
        :input  : bool - Boolean - True or False entered from user

        :return : String - "is" or "is not"
    """
    if bool == True:
        return "is"
    else:
        return "is not"

def displayTriangle(t):
    """
    Display the properties of the triangle object
    """
    print("The area is {}.".format(t.getArea()))
    print("The perimeter is {}.".format(t.getPerimeter()))
    print("The color of the triangle is {}".format(t.getColor()))
    print("The Triangle {} filled."
        .format(getFilledString(t.isFilled())))

def getTriangle(props):
    """
    Description: Creates a triangle object based on user input properties
        : input : props: List - user entered parameters

        : return : triangle: Triangl
    """
    s1,s2,s3,color,filled = props
    triangle = Triangle(s1,s2,s3)
    triangle.setColor(color)
    triangle.setFilled(filled)

    return triangle

if __name__ == '__main__':
    # Get trianle properties
    triangleProps = getTriangleProperties()

    # caluclate and display trianlgle props
    displayTriangle(getTriangle(triangleProps))
