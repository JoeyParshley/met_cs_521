"""
   Joey Parshley
   MET CS 521 O2
   26 MAR 2018
   hw_2_2_5
   Write a program that reads the subtotal and the gratuity rate and computes 
   the gratuity and total.
 """

# Greet the user and prompt them for a measurement in feet
print('\nThis program reads the subtotal and the gratuity rate and '\
    'computes the gratuity and total.\n')

subtotal, gratuity_rate = input("Please enter the subtotal and a gratuity "\
    "rate separated by a space without punctutation: " ).split()
try:
    subtotal = float(subtotal)
except ValueError:
    print("\nSorry I was expecting a number for the subtotal."\
        "Please try again. \n")
try:
    gratuity_rate = float(gratuity_rate)
except ValueError:
    print("\nSorry I was expecting a number for the gratuity_rate such as "\
        "'15'. Please try again. \n")


def get_gratuity (subtotal):
    """
    Description: calculate the gratuity based on the subtotal
      :input param : subtotal - amount of bill

      :return: gratuity by the formula:
          gratuity_rate/100 * subtotal
    """
    return (gratuity_rate / 100) * subtotal

# Calculate the total of the bill 
total = subtotal + get_gratuity(subtotal)

# Display the converted temperature to the console.
print(
    "\nThe gratuity is ${0:,.2f} and the total bill is ${1:,.2f}.\n"
    .format(gratuity_rate, total)
)