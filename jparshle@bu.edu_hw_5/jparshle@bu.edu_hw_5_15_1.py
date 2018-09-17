"""
   Joey Parshley
   MET CS 521 O2
   10 APR 2018
   hw_5_15_1
   Description: Write a recursive function that computes the sum of the digits
   in an integer. Use the following function header:

   def sumDigits(n):

   Write a test program that prompts the user to enter an integer and displays
   its sum.

   For example, sumDigits(234) returns 2 + 3 + 4 = 9

"""

# define the sumDigits method


def sumDigits(n):
    digitSum = 0
    if len(str(n)) == 1:
        return n
    else:
        return digitSum + (n % 10) + sumDigits( n // 10 )

if __name__ == '__main__':
    invalid_entry = True
    if __name__ == '__main__':
        # prompt user to enter integer verify that it is an integer
        msg = "{} is not an integer and the total of the digits won't be computed."
        while invalid_entry:
            try:
                inp = input("Enter a integer: ")
                n = int(inp)
                invalid_entry = False
            except:
                print(msg.format(inp))

        # Display the sum of the digits
        print("The sum of the digits in {0} is {1}.\n".format(n, sumDigits(n)))

