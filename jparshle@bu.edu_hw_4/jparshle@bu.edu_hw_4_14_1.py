"""
   Joey Parshley
   MET CS 521 O2
   3 APR 2018
   hw_4_14_1
   Description: Revise Listing 14.4 CountKeywords.py to display the keywords in
                a Python source file as well as to count the number of the 
                keywords.

    Note the body of listing 14.4 is used below with modifications for this
    assigment.

                
"""
import os.path
import sys

def trimmed_set_to_string(s):
    """
        Description: covert a set to a printable string with the bracket 
        stripped off

        : input : s - set to be converted
        : return : st - string with open closing brackets stripped off
    """
    # convert set to a string and remove first and last character
    st = str(s)[1:-1]
    return st

def main():
    keyWords = {"and", "as", "assert", "break", "class", 
      "continue", "def", "del", "elif", "else",
      "except", "False", "finally", "for", "from",
      "global", "if", "import", "in", "is", "lambda",
      "None", "nonlocal", "not", "or", "pass", "raise",
      "return", "True", "try", "while", "with", "yield"}

    filename = input("Enter a Python source code filename: ").strip()

    if not os.path.isfile(filename): # Check if file exists
        print("File", filename, "does not exist")
        sys.exit()

    infile = open(filename, "r") # Open files for input 

    text = infile.read().split() # Read and split words from the file 

    count = 0
    # create an empty set to hold the used keywords
    used_words = set()
    for word in text:
        if word in keyWords:
            count += 1
            # add the word to the used_keyword set
            used_words.add(word)

    # display the count of the keyword for the file and list them out.
    print("There are {0} keywords used in {1}, these keywords are: {2}."
        .format(count, filename, trimmed_set_to_string(used_words)))

main()