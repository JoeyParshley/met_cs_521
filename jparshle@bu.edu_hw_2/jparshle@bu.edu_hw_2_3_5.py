"""
   Joey Parshley
   MET CS 521 O2
   26 MAR 2018
   hw_2_3_5
   Description: This program will calulate and display the are of a 
   regular polygon. It will ask the user for the number of sides and the
   lenght of these sides and will return the area of the polygon.

   The length of the sides will be calculated via:

   s = 2r sin(pi/5) with r being the distance from the center to the vetex

   The Area will be calculated via:

   A = (3 * sqrt(3) / 2) * s ^2 where s is the length of the side calculated
   above
 """
# impor the math module to use pi and tan()
import math
import sys
# greet the user
print("\nThis program will calulcate the area of a regular polygon "\
    "based on the number of sides and lenght of a side.\n")

# get the number of sides
try:
    number_of_sides = int(input("Enter the number of sides: "))
except ValueError:
    print("\nSorry, you need to enter an integer for the number of sides.\n")
    sys.exit()

try:
    side_length = float(input("Please enter the length of a side: "))
except ValueError:
    print("\nSorry, you need to enter a number for the side length.\n")
    sys.exit()

def get_area(sides, length):
    """
    defintions: calculates the area of a regular polygon
      :input param: sides - number of sides of the polygon
      :input param: length - length of sides of the polygon

      :output param: area of the polygon
    """
    numerator = sides * length * length
    denominator = 4 * math.tan(math.pi/sides)
    area = numerator / denominator

    return area

print(
    "The are of a regular polygon with {0:g} sides of {1:g} length is {2:,.2f}.\n"
    .format(number_of_sides, side_length, get_area(number_of_sides,side_length) ))
