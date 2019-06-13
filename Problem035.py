# Circular primes

# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

import time, math
from itertools import permutations

s = time.time()

count = 0


def is_prime(num):
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	else:
		return True


def get_rotations(num):
	li = []
	li.append(num)
	num = str(num)
	for i in range(len(num)-1):
		num = num[len(num)-1] + num[:-1]
		li.append(int(num))
	return li


for num in range(2, 1000000):
	if is_prime(num):
		l = get_rotations(num)
		
		for i in l:
			if not is_prime(i):
				break
		else:
			count += 1
			print(num)

# l = permutations(str(5439))
# for i in l:
# 	n = int(''.join(i))
# 	print(n)


print("Total circular primes: ", str(count))
print(time.time()-s)
