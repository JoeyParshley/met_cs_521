def pent(n):
	if n == 1:
		return 1
	else:
		# return n + sum( n - 1 )
		return pent(n-1) + (3 * (n - 2))

n = int(input("Enter a positive integer: "))

print("The polygon {0} is {1}".format(n, pent(n)))