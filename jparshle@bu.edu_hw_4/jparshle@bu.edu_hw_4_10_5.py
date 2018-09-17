"""
   Joey Parshley
   MET CS 521 O2
   3 APR 2018
   hw_4_10_5
   Description: Write a program that reads in numbers separated by a space in
   one line and displays distinct numbers (i.e., if a number appears multiple
   times, it is displayed only once). (Hint: Read all the numbers and store them
   in list1 . Create a new list list2 . Add a number in list1 to list2 . If the
   number is already in the list, ignore it.) Here is the sample run of the 
   program:

   Enter ten numbers: 1 2 3 2 1 6 3 4 5 2  
    
    The distinct numbers are: 1 2 3 6 4 5
    
"""
N = 10
invalid_entry = True

while invalid_entry:
  list1 = input("Enter {} numbers separated by a space: ".format(N)).split()

  assert len(list1) == N, '{} values not provided!'.format(N)

  for n in list1:
    try:
      n = int(n)
      invalid_entry = False
    except:
      print("Error: All {} values are not integers!".format(N))
      invalid_entry = False

def get_destinct_numbers(l1):
  """
  Descriptin: gets the distinct numbers from a list of numbers
    :input l1
  """
  l2 = [ ]
  lst = [ num for num in list1]
  for x in lst:
     if x not in l2:
       l2.append(x)
  return " ".join(l2)

# print("The distinct numbers are {0}".format(" ".join(list2)))
print("The distinct numbers are {0}".format(get_destinct_numbers(list1)))
