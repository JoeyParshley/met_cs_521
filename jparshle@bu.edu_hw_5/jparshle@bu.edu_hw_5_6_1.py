"""
   Joey Parshley
   MET CS 521 O2
   10 APR 2018
   hw_5_6_1
   Description: Description: Write a function with the following header that 
   returns a 
   pentagonal number.

   def getPentagonalNumber(n):

   Write a test program that uses this function to display 
   the first 100 pentagonal numbers with 10 numbers on each line.

   A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2, . . . 

"""

# define the getPentagonalNumber method
def getPentagonalNumber(n):
    """
    Description: Calculates the pentagonal number for a given number via the
    equation:

                n( 3n - 1 )/2

        :input : n - number to be used to calculate the pentagonal number
        :return : pentagonal number
    """
    return (n * ( (3 * n) - 1))/2


# Constants to intialize the num list and set rows and columns of table data
num = 0
ROWS = 10
COLS = 10

if __name__ == '__main__':
    # Display results 10 numbers per line
    print("\nThe first {} pentagonal numbers are:\n".format(ROWS * COLS))
    for row in range (ROWS + 1):
        for col in range (COLS + 1):
            print('{0:>8,d}'
                .format( int( getPentagonalNumber(num) ) ), end=' ')
            num += 1
        print() 