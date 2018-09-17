"""
   Joey Parshley
   MET CS 521 O2
   10 APR 2018
   hw_5_11_11
   Description: Write a program that prompts the user to enter a number between 
   0 and 511 and displays the corresponding 3 × 3 matrix with the characters 
   H and T . Here is a sample run:

   You can represent the state of the coins with the values 0 (heads) and
   1 (tails). Here are some examples:


    0 0 0    1 0 1    1 1 0    1 0 1    1 0 0   
    0 1 0    0 0 1    1 0 0    1 1 0    1 1 1   
    0 0 0    1 0 0    0 0 1    1 0 0    1 1 0

    Each state can also be represented using a binary number. For example, 
    the preceding matrices correspond to the numbers:

    000010000 101001100 110100001 101110100 100111110
	There are a total of 512 possibilities. So, you can use the decimal 
	numbers 0 , 1 , 2 , 3 , ..., and 511 to represent all states of the matrix. 

   Sameple output:
   Enter a number between 0 and 511: 7

    H H H 
    H H H 
    T T T

"""