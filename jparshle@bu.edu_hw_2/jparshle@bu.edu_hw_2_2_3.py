"""
   Joey Parshley
   MET CS 521 O2
   26 MAR 2018
   hw_2_2_3
   Write a program that reads a number in feet, converts it to meters, and 
   displays the result.
     One foot is 0.305 meters.
 """

# Greet the user and prompt them for a measurement in feet
print("\nThis program will read a measurement in feet from the console and "\
    "convert the result to meters and display the result.\n")
# get the measurement from the user
try:
    feet = float(input("Please enter your length in feet: "))
except ValueError:
    print("\nSorry I was expecting a number. Please try again. \n")

# Convert the length from feet to meters
meters = feet * 0.305

# Display the converted temperature to the console.
print("\n{0:g} feet is equal to {1:,.2f} meters.\n".format(feet, meters))