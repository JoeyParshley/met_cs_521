"""
   Joey Parshley
   MET CS 521 O2
   30 MAR 2018
   hw_3_4_3
   Description: Write a program that solves a 2 x 2 linear equation Cramer's
                rule:

                ax + by = e        x = (ed - bf)/(ad - bc)
                cx + dy = f        y = (af - ec)/(ad - bc)

                Prompts the user to enter a , b , c , d , e , and f and 
                display the result. 
                If ad – bc is 0 , report that The equation has no solution.

"""
import sys
import math
invalid_entry = True

ERROR_MESSAGE = "\nYour entry '{0}' is not a number. Please try again."

def get_x():
    return ((e * d) - (b * f)) / numerator

def get_y():
    return ((a * f) - (e * c)) / numerator

# prompt the user
while invalid_entry:
    a, b, c, d, e, f = input("\nEnter a, b, c, d, e, f: ").split(',')
    # print(values)

    for val in a, b, c, d, e, f:
        try:
          val = float(val)
          invalid_entry = False
        except ValueError:
          print(ERROR_MESSAGE.format(val))
          invalid_entry = True

a, b, c, d, e, f = float(a), float(b), float(c), float(d), float(e), float(f)
numerator = (a * d) - (b * c)

if (numerator) == 0:
    print("This equation has no solution.")
else:
    print("x is {0:.2g} and y is {1:.2g}".format(get_x(),get_y()))