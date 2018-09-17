"""
   Joey Parshley
   MET CS 521 O2
   10 APR 2018
   hw_5_15_3
   Description: Write a recursive function to find the GCD
   (greatest common divisor).
   Write a test program that prompts the user to enter two integers and 
   displays their GCD.

   The gcd(m, n) can also be defined recursively as follows:
    If m % n is 0 , gcd(m, n) is n .
    Otherwise, gcd(m, n) is gcd(n, m % n) 

"""
import sys
N = 2
# define gcd method
def gcd(m,n):
    m_mod_n = m % n
    if m_mod_n == 0:
        return n
    else:
        return gcd(n, m_mod_n)

if __name__ == '__main__':
    # ask for and read two integers
    inp = input("Enter a two integers separated by space: ")

    # split the inp and convert to integers
    lst = []
    inp = inp.split()
    msg = '{} is not an integer and the GCD will not be computed.'
    countMsg = '{} integers were not entered'

    for i in inp:
        # convert the inp to integer
        try:
            lst.append(int(i))
        except:
            lst.append(-1)
            print(msg.format(i))

    # Make sure we have two integers
    if len(lst) != N:
        print(countMsg.format(N))
        sys.exit()  

    # Display the GCD of the digits
    print("The gcd of the digits {0} and {1} is {2}.\n".format(lst[0], lst[1], gcd(lst[0],lst[1])))
