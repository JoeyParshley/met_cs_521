def fib(n):
	if n == 0:
		return 0

	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

n = int(input("Enter a positive integer: "))

print("The fibonazzi of {0} is {1}".format(n, fib(n)))