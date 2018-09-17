"""
   Joey Parshley
   MET CS 521 O2
   26 MAR 2018
   hw_2_3_3
   Description: Compute the estimated enclosed by Atlanta, Georgia; Orlando, 
   Florida; Savannah, Georgia; and Charlotte, North Carolina based on the
   GPS locations obtained from www.gps-data-team.com/map/
 """
import math
# greate global variable for each city pointing to tuple of the gps coordinates
atlanta = (33.7489954,-84.3879824)
orlando = (28.5383355,-81.37923649999999)
savannah = (32.0835407,-81.09983419999998)
charlotte = (35.2270869,-80.84312669999997)

def deg_to_radians(degrees):
    """
    Description: converts degrees to radians
      :input    : degree location represented as degrees
      :returns  : radians
    """
    return math.radians(degrees)

# compute the distance between each city
def distance_between(city_1,city_2):
    """
    Description: Calulate the distance on the globe between two cities
      in the form of the tuple (latitude andlongitude). Uses the average radius
      of the earth as 6371.01 km

      :input param  : city_1 - tuple of coords for first city
      :input param  : city_1 - tuple of coords for first city

      :returns      : distance between two cities calucated by 
                      equation below
                    
      d = radius x acos(sin(x1) x sin(x2) + cos(x1) x cos(x2) x cos(y1-y2))

    """
    # CONSTANT - average radius of earth
    RADIUS = 6371.01
    # use local variable to hols latitude and longitude of each city in radians
    x1, y1 = math.radians(city_1[0]), math.radians(city_1[1])
    x2, y2 = math.radians(city_2[0]), math.radians(city_2[1])

    #calculate distance between cities
    distance = RADIUS * math.acos(
        (math.sin(x1) * math.sin(x2)) + (
            math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)
        )
    )

    # return the calculated distance
    return distance

def get_triangle_area(s1, s2, s3):
    """
    Definition: calculates the area of a triangle of sides s1, s2, and s3
      input param: s1 - side one of triangle
      input param: s2 - side two of triangle
      input param: s3 - side three of triangle

      output param: area - area of triangle
    """
    s = (s1 + s2 + s3) / 2
    area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

    return area

"""
break area into two triangles as follows
  triangle one:
   side1 = atl_to_orl
   side2 = orl_to_sav
   side3 = sav_to_atl

  triangle two:
   side1 = atl_to_cha
   side2 = cha_to_sav
   side3 = sav_to_atl
"""
# Get ditances between cities
atl_to_orl = distance_between(atlanta,orlando)
orl_to_sav = distance_between(orlando,savannah)
sav_to_atl = distance_between(savannah,atlanta)
atl_to_cha = distance_between(atlanta,charlotte)
atl_to_cha = distance_between(charlotte,savannah)

# calulated area of each triangle using city distances as sides
area1 = get_triangle_area(atl_to_orl, orl_to_sav, sav_to_atl)
area2 = get_triangle_area(atl_to_cha, sav_to_atl, sav_to_atl)

# Total area is combined area of two triangles
area = area1 + area2

# Display the result to the console
print("\nThe area enclosed by Atlanta, Georgia; Orlando, Florida; "\
    "Savannah, Georgia; and Charlotte, North Carolina is {0:,.2f} km^2.\n"
    .format(area))
