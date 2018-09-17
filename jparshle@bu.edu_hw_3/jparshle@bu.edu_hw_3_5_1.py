"""
   Joey Parshley
   MET CS 521 O2
   30 MAR 2018
   hw_3_5_1
   Description: This program reads an unspecified number of integers, 
                determines howmany positive and negative values have been read,
                and computes the total and average of the input values 
                (not counting zeros).

                The program ends with the input 0. 

    input params: integers read from the console until user enters 0  

    output:       total - total of all the non zero integers entered
                  negative_count - count of negative integers
                  positive_count - count of positive integers
                  non_zeros_count - count of nonzero integers



 """
# Get the numbers from the user making sure that they are integers
try:
    data = int(input("Enter an integer, the input ends if it is 0: "))
except ValueError:
    print("\nSorry I was expecting an integer. Please try again. \n")

# Iinitialize the variables 
total = negative_count = positive_count =  non_zeros_count = 0

# loop the data request until the user enters
while data != 0:
    # increment total and non_zeros count for all non zero entries
    # increment positve and negative counts when data is positive of negative
    if data > 0:
        non_zeros_count += 1
        positive_count += 1
        total += data
    elif data < 0:
        non_zeros_count += 1
        negative_count += 1
        total += data
    try:
        data = int(input("Enter an integer, the input ends if it is 0: "))
    except ValueError:
        print("\nSorry I was expecting an integer. Please try again. \n")

# get the average of all the integers entered
average = total / non_zeros_count

print("\nThe number of positives is {0:d}".format(positive_count))
print("The number of negatives is {0:d}".format(negative_count))
print("The total is {0:d}".format(total))
print("The average is {0:.2f}".format(average))
