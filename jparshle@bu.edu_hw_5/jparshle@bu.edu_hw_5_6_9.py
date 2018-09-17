"""
   Joey Parshley
   MET CS 521 O2
   10 APR 2018
   hw_5_6_9
   Description: Write a module that contains the following two functions:

   # Converts from feet to meters

   def footToMeter(foot):
   # meter = 0.305 * foot

   # Converts from meters to feet
   def meterToFoot(meter):
   # foot = meter / 0.305

   Write a test program that invokes these functions to display the following
   tables:

   Feet       Meters    |    Meters       Feet
    
    1.0        0.305     |    20.0         66.574 
    2.0        0.610     |    25.0         81.967
    ...
    9.0        2.745     |    60.0         196.721
    10.0       3.050     |    65.0         213.115

"""
FOOT_METER_CONVERSION_FACTOR = 0.305
START = 20
END = 66
STEP = 5
FEET = 'feet'
METERS = 'meters'

def footToMeter(foot):
    """
    Description: converts the a measurement from feet to meters by the equation
        foot = meter / 0.305
    :input foot : Float - foot amount to be converted to meter
    :return meter : Float - foot converted to meters
    """
    meter = foot * FOOT_METER_CONVERSION_FACTOR

    return meter

def meterToFoot(meter):
    """
    Description: converts the a measurement from meters to feet by the equation
        meter = 0.305 * foot
    :input meter : Float - meter amount to be converted to feet
    :return foot : Float - meter converted to feet
    """
    foot = meter / FOOT_METER_CONVERSION_FACTOR

    return foot

if __name__ == '__main__':
    # print the table header
    print("{0:<8} {1:>8}     |     {1:<8} {0:>8} ".format(FEET,METERS))
    # use the idx property of the loop for the foot column
    # use 'l' loop variable for the meter
    for idx, l in enumerate(range(START, END,STEP)):
        feet = idx + 1
        meter = l
        print("{0:<8.1f} {1:>8.3f}     |      {2:<8.1f} {3:>8.3f}"
        .format(feet, footToMeter(feet), meter, meterToFoot(meter)))
