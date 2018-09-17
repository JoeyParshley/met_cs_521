"""
   Joey Parshley
   MET CS 521 O2
   30 MAR 2018
   hw_3_8_1
   Description: Write a program that prompts the user to enter a Social Security
    number in the format ddd-dd-dddd, where d is a digit. The program displays 
    Valid SSN for a correct Social Security number or Invalid SSN otherwise.
 """

def ssn_validation (ssn_entry):
    """
    Decription: determine if the string is a valid ssn in the format:
    ddd-ddd-dddd
        :input param : ssn_entry - string to validated as a ssn

        :validation_string - string stating the validity of entry
    """
    if len(ssn_entry) != 11:
        validation_string = "\nInvalid SSN\n"
    else:
        # loop through ssn_entry and test that each character is a digit
        for char in ssn_entry:
            # skip the dashes
            if char is '-':
                continue
            else:
                # if you can convert the char to int it is a digit and 
                # valid so far
                try:
                    is_digit = int(char)
                    validation_string = "\nValid SSN\n"
                # as soon as you cannot convert a character to a digit 
                # its invalid
                except:
                    validation_string = "\nInvalid SSN\n"
                    break
    return validation_string

invalid_entry = True

#prompt the user for a social security number with hyphens
while invalid_entry:
    ssn_entry = input("\nPlease enter a Social Security Number in the "
        "format ddd-dd-dddd: ")
    # if ssn_entry has no dashes keep asking
    invalid_entry = ssn_entry.find('-') is -1

# output ssn validity to the console
print(ssn_validation(ssn_entry))
