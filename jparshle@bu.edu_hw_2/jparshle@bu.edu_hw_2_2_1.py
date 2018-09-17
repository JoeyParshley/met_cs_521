"""
   Joey Parshley
   MET CS 521 O2
   26 MAR 2018
   hw_2_2_1
   Write a program that reads a Celsius degree from the console and converts 
   it to Fahrenheit and displays the result. The formula for the conversion
   is as follows:
       fahrenheit = (9 / 5) * celsius + 32
 """

# Greet the user and prompt them for a temperature in celsius
print("\nThis program will read a temperature in celsius from the console and "\
    "convert the result to fahrenheit and display the result.\n")

try:
    celsius = float(input("Please enter your temperature in celsius: "))
except ValueError:
    print("\nSorry I was expecting a number. Please try again. \n")
"""
CONSTANTS: C_TO_F_MULTIPLIER - mutiplier to use in conversion of the celsius 
             to fahrenheit
           C_TO_F_OFFSET - offset to use in conversion of the celsius to 
             fahrenheit
"""
C_TO_F_MULTIPLIER = 9 / 5
C_TO_F_OFFSET = 32

# Convert the celsius temperature to fahrenheit
fahrenheit = (C_TO_F_MULTIPLIER * celsius) + C_TO_F_OFFSET

# Display the converted temperature to the console.
print("\n{0:g}°C is equal to {1:g}°F\n".format(celsius, fahrenheit))
