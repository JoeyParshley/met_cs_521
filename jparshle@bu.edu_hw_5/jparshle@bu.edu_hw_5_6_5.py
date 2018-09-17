"""
   Joey Parshley
   MET CS 521 O2
   10 APR 2018
   hw_5_6_5
   Description: Write the following function to display three numbers in 
   increasing order

   def displaySortedNumbers(num1, num2, num3):

   Write a test program that prompts the user to enter three numbers and
   invokes the function to display them in increasing order. 

"""
N = 3
invalid_entry = True
# define the displaySortedNumbers method
def formatNum(n):
    """
    Description: Formates a number string as a integer if there is '.0'
        :input : n - Float -number to be formatted 
        :return : String - if the number will end in a .0 it will be truncated
                    otherwise the decimal portion is kept
    """
    if n == int(n):
        return str(int(n))
    else:
        return str(n)

def formatList(l):
    """
    Description: Formats a list of elements into a comma separated string
        :input : l - List - list of elements to be formatted
        :return : st - String - element formated into a comma separated string
    """
    st = ', '.join(str(e) for e in l)
    return st

def displaySortedNumbers(num1, num2, num3):
    """
    Description: Displays a user inputted numbers sorted in ascending order
        :input : num1, num2, num3 - 
    """
    numList = [formatNum(num1), formatNum(num2), formatNum(num3)]
    sortList = [n for n in numList]
    sortList.sort()

    print("The numbers:[ {0} ] sorted in increasing order are: [ {1} ]".
        format(
            formatList(numList), 
            formatList(sortList)
            )
        )

if __name__ == '__main__':
    countErrorMsg = "You did not provide {} values!\n"
    typeErrorMsg = "Error: All {} are not numeric!"

    while invalid_entry:
        # prompt user for three numbers
        inp = input("Enter {} numbers separated by spaces: ".format(N))
        parsed = inp.split()
        # verify that there are three entries
        assert len(parsed) == N, countErrorMsg.format(N)

        # verify that they are all numbers
        try:
            n1, n2, n3 = list(map(float, parsed))
            invalid_entry = False
        except:
            print(typeErrorMsg.format(N))

    # display the numbers in increasing order
    displaySortedNumbers(n1, n2, n3)