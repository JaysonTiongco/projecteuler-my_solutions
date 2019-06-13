# Problem10 - Summation of Primes
#
# The sum of primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math, time

s = time.time()

num = 1
total = 0

while num < 2000000:
	num += 1
	for i in range(2, int(math.sqrt(num)) + 1):
		if (num % i) == 0:
			break
	else:
		total += num

print(total)
print(time.time() - s)

# Solved:
# ans: 142913828922
# time: 216.19820094108582
# using dualcore 1.6ghz
