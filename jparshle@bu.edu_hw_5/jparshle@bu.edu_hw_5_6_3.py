"""
   Joey Parshley
   MET CS 521 O2
   10 APR 2018
   hw_5_6_3
   Description: Palindrome integer - Write a test program that prompts the user
   to enter an integer and reports whether the integer is a palindrome.

   A number is a palindrome if its reversal is the same as itself.

   Write the functions with the following headers:
   # Return the reversal of an integer, e.g. reverse(456) returns  # 654

   def reverse(number):
    
        # Return true if number is a palindrome
    
    def isPalindrome(number):

        # Use the reverse function to implement isPalindrome 
"""
invalid_entry = True
# define reverse method
def reverse(number):
    """
    Description: returns the reverse of an entered number
        input: number - integer to be reversed
        return: rebmun - integer in reverse order
    """
    rebmun = ''.join(list(str(number))[::-1])
    return str(rebmun)

def isPalindrome(number):
    """
    Description: Determines is a given string is a palidrome meaning is the 
    same backwards as it is forwards
        :input: number - String string version of number to be converted
        :return: sub_string - String to be used in string returned to user
                              empty if it is a panilndrone and "not" if it
                              is not a palinforme
    """
    if len(str(number)) == 1:
        return ''
    elif str(number) == reverse(number):
        return ''
    else:
        return 'not '

if __name__ == '__main__':
    # prompt user to enter integer verify that it is an integer
    msg = '{} is not an integer and its integer palindromeness cannot be determined.\n'
    while invalid_entry:
        try:
            inp = input("Enter an integer: ")
            n = int(inp)
            invalid_entry = False
        except:
            print(msg.format(inp))

    # display if the number is a palindrome
    print("\n{0} is {1}a palindrome integer.\n".format(n, isPalindrome(n)))
