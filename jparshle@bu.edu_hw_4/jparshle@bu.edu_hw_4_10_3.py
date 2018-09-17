"""
   Joey Parshley
   MET CS 521 O2
   3 APR 2018
   hw_4_10_3
   Description: Write a program that reads some integers between 1 and 100 and 
                counts the occurrences of each.

                Enter integers between 1 and 100: 2 5 6 5 4 3 23 43 2  
    
    2 occurs 2 times
    3 occurs 1 time
    4 occurs 1 time
    5 occurs 2 times
    6 occurs 1 time
    23 occurs 1 time
    43 occurs 1 time
 """
invalid_entry = True
ERROR_MESSAGE = "\nYour entry '{0}' is not a number. Please try again."

def get_count(l,i):
    """
    Description: gets the count of integers in a list
        :input : l - list that contains the integers
        :input : i - integer to be counted

        :return : the count of integer in the list
    """
    return l.count(i) 

def display_integer_counts(l):
    """
    Description: get the integer count and displays it to the console
        :input : l list containing the itegers
    """
    for integer in l:
        print("{0} occurs {1} time".format(integer, get_count(l, integer)))

while invalid_entry:
    entry_list = input("Enter integers between 1 annd 100: ").split()

    for entry in entry_list:
        try:
            entry = int(entry)
            invalid_entry = False
        except ValueError:
            print(ERROR_MESSAGE.format(entry))
            invalid_entry = True
        else:
            if (entry < 0) or (entry > 100):
                print("Number out of range")
                invalid_entry = True

display_integer_counts(entry_list)
