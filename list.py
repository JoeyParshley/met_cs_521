lst = [1,2,3,4,5,6]
for i in range(1,6):
  print("i is {0}".format(i))
  print("i - 1 is {0}".format(i - 1))
  print("lst[i] is {0}".format(lst[i]))
  print("lst[i-1] is {0}".format(lst[i-1]))
  lst[i] = lst[ i - 1]
print(lst)


