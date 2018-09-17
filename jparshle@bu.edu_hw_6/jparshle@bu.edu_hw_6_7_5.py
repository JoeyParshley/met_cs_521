"""
   Joey Parshley
   MET CS 521 O2
   17 APR 2018
   hw_6_7_5
   Description: Design a class named RegularPolygon that contains:
                :   A private int data field named n that defines the number of 
                    sides in the polygon.
                :   A private float data field named side that stores the 
                    length of the side.
                :   A private float data field named x that defines the 
                    x-coordinate of the center of the polygon with default 
                    value 0 .
                :   A private float data field named y that defines the 
                    y-coordinate of the center of the polygon with default 
                    value 0 .
                :   A constructor that creates a regular polygon with the 
                    specified n (default 3 ), side (default 1 ), x (default 0 ), 
                    and y (default 0 ).
                :   The accessor and mutator methods for all data fields.
                :   The method getPerimeter() that returns the perimeter of 
                    the polygon.
                :   The method getArea() that returns the area of the polygon. 
                    The formula for computing the area of a regular polygon is 
                    Area Area= n×s^2 / 4×tan(π/n)

                :   Write a test program that creates three RegularPolygon
                    objects, created using RegularPolygon() , using 
                    RegularPolygon(6, 4) and RegularPolygon(10, 4, 5.6, 7.8) . 
                :   For each object, display its perimeter and area.

"""
from regularPolygon import RegularPolygon
def displayPolys(p):
    """
    Description: Displays the properties of a list of polygons in tabular data

        :input : p - List, list of polygons to be displayed
        :output: None
    """
    # print header
    print("{0:<12}{1:<12}{2:<12}".format('Polygon','Perimeter','Area'))
    # print properties for each polygon object
    for idx, poly in enumerate(p):
        print("{0:4}{1:12}{2:12.2f}"
            .format(idx + 1, poly.getPerimeter(), poly.getArea()))

if __name__ == '__main__':
    # Create a list of polygons to be tested
    polygons = [ 
        RegularPolygon(), 
        RegularPolygon(6, 4), 
        RegularPolygon(10, 4, 5.6, 7.8)
    ]

    # Display regularPolygon data
    displayPolys(polygons)
