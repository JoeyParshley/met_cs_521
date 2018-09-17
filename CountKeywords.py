import os.path
import sys

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
    used_words = {}
    for word in text:
        if word in keyWords:
            count += 1
            used_words.add(word)

    print("The number of keywords in", filename, "is", count)
    print("The keywords used in {0} are {1}".format(filename, str(used_words)))

main()