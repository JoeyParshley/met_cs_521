def x_to_the(n):
	if n == 0:
		return 1
	else:
		return x * x **( n -1 )

n = int(input("Enter a positive integer: "))
x = float(input("Enater a real number: "))

print("{0:g} raised to the power of {1:d} is {2:g}".format(x, n, x_to_the(n)))