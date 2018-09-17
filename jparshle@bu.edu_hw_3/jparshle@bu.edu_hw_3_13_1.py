"""
   Joey Parshley
   MET CS 521 O2
   30 MAR 2018
   hw_3_13_1
   Description: Write a program that removes all the occurrences of a specified 
   string from a text file. Your program should prompt the user to enter a 
   filename and a string to be removed. Here is a sample run:
   Here is a sample run:

    Enter a filename: test.txt  
    
    Enter the string to be removed: morning  
    
    Done
 """
import os.path
import sys
file_missing = True

def removeStringFromFile(file,string):
    """
    Description: remove all occurences of a string from a file
        :input param : String - filename to be opened
        :input param : String - string to be removed from file
        :return :  string consisting of the contents of the file with 
                    the string removed 
    """
    # is string is in file remove it
    if (string in open(file).read()):
        input = open(file,"r")
        input_contents = input.read()
        # remove the string from the file
        result = input_contents.replace(string,'')
        # close the file
        input.close()
        return result
    else:
        print("{0} is not in {1}".format(string,file))

# prompt user for a filename 
while file_missing:
    filename = input("\nEnter a filename: ").strip()
    # check to see if filename exists
    if os.path.isfile(filename):
        # prompt user for the string to be removed
        file_missing = False
        string_to_be_removed = input("\nEnter the string to be removed: ")
        # remove the string from the file and store the result
        result = removeStringFromFile(filename,string_to_be_removed)
    else:
        print("\n That file does not exist.")
