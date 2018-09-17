"""
   Joey Parshley
   MET CS 521 O2
   3 APR 2018
   hw_4_11_1
   Description: Write a function that returns the sum of all the elements in a
   specified column in a matrix using the following header:

   def sumColumn(m, columnIndex):

    Write a test program that reads a 3 × 4 matrix and displays the sum of
    each column.

    Enter a 3-by-4 matrix row for row 0: 1.5 2 3 4  
    Enter a 3-by-4 matrix row for row 1: 5.5 6 7 8  
    Enter a 3-by-4 matrix row for row 2: 9.5 1 3 1  
    
    Sum of the elements for column 0 is 16.5
    Sum of the elements for column 1 is 9.0
    Sum of the elements for column 2 is 13.0
    Sum of the elements for column 3 is 13.0

"""

# constants representing rows (N) and columns (M) of a matrix
R = 3
C = 4

def getMatrix(rows,cols):
    """
    Description: build a matrix from row data given as user input
        :input param 
            : rows : Int - number of rows in the matrix
            : cols : Int - number of columns in each row

        :return param
            : m    : rows x cols matrix of user given numbers 
    """
    # intialize an empty list
    m = []
    # Prompt the user to enter each row
    for row in range(rows):
        entry = input("Enter {0} numbers for row {1} of a 3 - 4  matrix : "
            .format(cols, row)).split()
        row = [eval(num) for num in entry]
        # append each row to the matrix
        m.append(row)
    return m


def sumColumn(m, columnIndex):
    """
    Description: Calculate the sum of a column for a two dimensional matrix
        :input param 
            : m          :  LIST - two dimensional matrix containing the column
            :columnIndex :  Int - Index of the column to be summed

        : return param
            : total      : sum of the column values 
    """
    # intitialize the total
    total = 0
    for row in range(len(m)):
        # add the value from the current column to the total
        total += m[row][columnIndex]

    return total


# Prompt the user to enter each row
matrix = getMatrix(R,C)

for column in range( len( matrix[0] ) ):
    print("Sum of the elements for column {0} is {1:0.1f}"
        .format(column, sumColumn(matrix, column)))
