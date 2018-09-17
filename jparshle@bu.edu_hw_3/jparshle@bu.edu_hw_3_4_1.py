"""
   Joey Parshley
   MET CS 521 O2
   30 MAR 2018
   hw_3_4_1
   Description: Write a program that prompts a user to enter the values for
                a, b, and c of a quadratic equation of the form
                ax^2 + bx + c = 0, and displays the possible roots if the 
                equation base on the discriminant ( b^2 - 4ac ) of the equation
                to calculate the roots:

                  r1,r2 = (-b +/- sqrt(b^2 - 4ac))/2a

                If the discriminate is > 0 display the two roots.
                If the discriminate is < 0 display that it has no roots.
                If the discriminate is 0 display the one root.

"""
import sys
import math
invalid_entry = True
ERROR_MESSAGE = "\nYour entry '{0}' is not a number. Please try again."

def getDiscriminant (a, b, c):
    """
    Description: calculate the discriminant of a quadratic equation to used to
        how many roots the equation has.

        :input params: a, b, c - the constanst in the quadratic equation:
            ax^2 + bx + c = 0

        :returns : discriminant
    """
    return (b * b - (4 * a * c))

def getRoots ( a, b, sqrt_discriminant ):
    """
    Description: calculate a root of a quadratic equation

    :input param: a - x^2 multiplier of the quadratic equation
                  b - x multiplier of the quadratic equation
                  c - the offset of the quadratic equation
                  where the quadratic equation takes the form:
                    ax^2 + bx + c = 0
                  discriminant - b^2 -4ac portion of the root calculation
                    if this is 0 there will be only 1 real root for the equation
                    if this is > 0 there will be 2 real roots for the equation
                    if thus is < 0 there will be no real roots for the equation
    :return : root of the quadratic equation
    """
    return (-b + sqrt_discriminant) / ( 2 * a )

def getSqrtOfDisc(discriminant):
    """
    Description: calculates the square root of the discriminant used to
                 determine the root(s) of a quadratic equation
                 This allows to pass in the positive or negative square root of
                 the discriminant to calulate both roots of a quadratic
                 equation with one method

    :input param: discriminant
    :return : square root of the discriminant
    """
    return math.sqrt(discriminant)

# Ask for the input
while invalid_entry:
  a, b, c = input(
      "Please enter the comma separated values for a, b, c for "
      "a quadratic equation: "
  ).split(',')

  # make sure the are numbers and keep asking until they are
  for val in a, b, c:
      try:
          val = float(val)
          invalid_entry = False
      except ValueError:
          print(ERROR_MESSAGE.format(val))
          invalid_entry = True
          break

a,b,c = float(a),float(b),float(c)

# get the discriminant
discriminant = getDiscriminant(a,b,c)

# get and display the root(s) or the fact that there are no real roots.
if discriminant > 0:
    sqrt_discriminant = math.sqrt(discriminant)
    print('\nThe roots are {0:.3g} and {1:.3g}.\n'.format(
        getRoots(
            a,
            b,
            getSqrtOfDisc(discriminant)),
        getRoots(
            a,
            b,
            -getSqrtOfDisc(discriminant))
        ))
elif discriminant == 0:
    sqrt_discriminant = math.sqrt(discriminant)
    print('\nThe root is {0:.2f}.\n'.format(getRoots(a,b,sqrt_discriminant)))
else:
    print('\nequation has no real roots.\n')    
