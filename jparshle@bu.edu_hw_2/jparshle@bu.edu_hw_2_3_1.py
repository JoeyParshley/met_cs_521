"""
   Joey Parshley
   MET CS 521 O2
   26 MAR 2018
   hw_2_3_1
   Write a program that prompts the user to enter the length from the center of 
   a pentagon to a vertex and computes the area of the pentagon
 """

# import the math module to use sin and pi
import math 
# Contstants to be used in functions
# used to calculate pentagon side
TWO_SIN_PI_OVER_5 = 2 * math.sin(math.pi/5)
# used to calculate pentagon area
AREA_CONSTANT = (3 * math.sqrt(3)) / 2

# Greet the user and prompt them for a measurement in feet
print("\nThis program computes the area of a pentagon based on the distance" \
    "from the center of the prgram to a vertex.\n")

# Get the distance from the center of the pentagon to a vertex
try:
    vertex_distance = float(input("\nPlease enter the distance from the center of "\
        "the pentagon to the vertex: "))
except ValueError:
    print("\nSorry I was expecting a number for the distance to the vetex. " \
        "Please try again. \n")

def pentagon_side (r):
    """
    Description: Calculates the side length of a pentagon
      :input param :  r - represents the distance from the center of the pentagon
                      to a vertex

      :returns     :  length - represents the length of one of the sides of the
                      pentagon
     """
    # calculate the length based on the circumradius
    length = r * TWO_SIN_PI_OVER_5
    return length

def pentagon_area (r):
    """
     Description: Calculates the area of a pentagon based on the
      side of the pentgon 
                  
      Uses the equation:
        Area = (3 * sqrt(3) / 2) * s * s

      :input param  : r - represents the distance from the center of the pentagon
        to a vertex (circumradius) used to calculate the side of the pentagon.

      :returns      : area - represents the area of the pentagon
    """
    # calculate the pentagon side based on the circumradius (r)
    side = pentagon_side(r)
    # calculate the pentagon area based on the side (side)
    area = side * side * AREA_CONSTANT
    # return the area
    return area

# get area of the pentagon and display it to the console
area = pentagon_area(vertex_distance)
print(
    "\nThe area of a pentagon with a vertex distance of {0:g} is {1:,.2f}.\n"
    .format(vertex_distance, area))
