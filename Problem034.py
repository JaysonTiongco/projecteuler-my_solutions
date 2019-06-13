# Digit factorials

# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import time

s = time.time()

total = 0


def factorial(num):
	factorial = 1
	for i in range(num, 1, -1):
		factorial *= i
	return factorial


factorial_values = [factorial(i) for i in range(10)]


for i in range(3, 1000000):
	s = 0
	for l in str(i):
		val = factorial_values[int(l)]
		s += val

	if s == i:
		total += i
		print(i)


print(total)
print(time.time()-s)
