"""
   Joey Parshley
   MET CS 521 O2
   30 MAR 2018
   hw_3_5_3
   Description: Program displays a table the converts kilograms to pounds
                via 1 kg = 2.2 lb

                The kilogram amounts are the odd numbers from 1 to 199
"""
# print the header with Kilograms left justified and Pounds right Justified 
# allow of padding to add space betweencolumns
print("{0:<14}{1:14}".format("Kilograms","Pounds"))

# init kilogram to 1 for the while loop
kilogram = 1

# Loop until kilograms = 199
while kilogram <= 199:
    # display the kilogram and conveted pound justifed to match the header
    print("{0:<14}{1:6.1f}".format(kilogram,kilogram * 2.2))
    # increment kilogramby two to get the next odd value
    kilogram += 2
