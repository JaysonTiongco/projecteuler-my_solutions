# Lattice paths
# Problem 15 
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

import time

s = time.time()

def factorial(num):
	value = 1
	for i in range(2, num + 1):
		value *= i
	return value

def paths(grid_size):
	dividend = factorial(grid_size)
	divisor = factorial(int(grid_size/2))
	ans = dividend / (divisor ** 2)
	print(ans)

paths(40)
print(time.time() - s)
