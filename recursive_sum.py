def sum(n):
	if n == 0:
		return 0
	else:
		return n + sum( n - 1 )

n = int(input("Enter a positive integer: "))

print("The sum of positive integers up to {0} is {1}".format(n, sum(n)))