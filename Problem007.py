# Problem 7 - 10 001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math, time

s = time.time()

num = 1
counter = 0

while True:
	num += 1
	for i in range(2, int(math.sqrt(num)) + 1):
		if (num % i) == 0:
			break
	else:
		counter += 1
		#print(str(num) + ' ' + str(counter))
		if counter == 10001:
			print(str(num) + ' ' + str(counter))
			print(time.time() - s)
			break

# IMPROVED PROCESS EFFICIENCY
