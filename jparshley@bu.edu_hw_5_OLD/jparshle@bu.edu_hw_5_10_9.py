"""
   Joey Parshley
   MET CS 521 O2
   10 APR 2018
   hw_5_10_9
   Description: Write a test program that prompts the user to enter a list of
   numbers and displays the mean and standard deviation.  Store the individual 
   numbers using a list, so that they can be used after the mean is obtained.


   Program should contain following functions:

   def deviation(x):

   def mean(x):

Ex 5.46:
import math

COUNT = 10 # Total numbers
sum = 0 # Store the sum of the numbers
squareSum = 0 # Store the sum of the squares

# Create numbers, find its sum, and its square sum
for i in range(COUNT):
     # Get a new number
     number = eval(input("Enter a number: "))

     # Add the number to sum
     sum += number

     # Add the square of the number to squareSum
     squareSum += number ** 2 # Same as number*number

# Find mean
mean = sum / COUNT

# Find standard deviation
deviation = math.sqrt((squareSum - sum * sum / COUNT) / (COUNT - 1))

# Display result
print("The mean is", mean)
print("The standard deviation is", deviation)

"""