"""
   Joey Parshley
   MET CS 521 O2
   17 APR 2018
   hw_6_7_1
   Description: Design a class named Rectangle to represent a rectangle
                The class contains:
                :   Two data fields named width and height
                :   A constructor that creates a rectangle with the specified
                    width and height with defaults of 1 and 2 respectively
                :   A method named getArea() that returns the area of this
                    rectangle
                :   A method named getPerimeter() that returns the perimeter

                : Write a test program that creates two Rectangle objects—one 
                  with width 4 and height 40 and the other with width 3.5 and 
                  height 35.7 . 
                : Display the width, height, area, and perimeter of each 
                  rectangle in this order.

"""

from rectangle import Rectangle

def testRectangles(r):
  """
  Definition: Displays the results of the rectancle object.
    :input param: r : Object - rectabgle to be tested
  """

  # Print table header
  print("{0:<12} {1:<12} {2:<12} {3:<12} {4:<12}"
    .format('Rectangle','Width','Height','Area','Perimeter'))
  # Print id, width, height, area and perimeter for each rectangle object
  for idx, rect in enumerate(r):
    print("{0:4}{1:12}{2:14}{3:14.2f}{4:14.2f}"
      .format(
        idx + 1, 
        rect.get_width(), 
        rect.get_height(), 
        rect.get_area(), 
        rect.get_perimeter()
      )
    )

if __name__ == '__main__':
  # Create a rectangle with width 4 and height 40
  rectangle1 = Rectangle( 4, 40 )
  # Create a rectangle with width 4 and height 40
  rectangle2 = Rectangle( 3.5, 35.7)

  # Display rectangle data
  testRectangles([rectangle1, rectangle2])
