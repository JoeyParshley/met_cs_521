def two_to_the(n):
	if n == 0:
		return 1
	else:
		return 2 * 2 **( n -1 )

n = int(input("Enter a positive integer: "))

print("2 raised to the power of {0} is {1}".format(n, two_to_the(n)))