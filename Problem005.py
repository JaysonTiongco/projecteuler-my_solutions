# Problem 5 - Smallest Multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

s = time.time()

num = 2520

cont = False
br = False

list_range = [11, 13, 14, 16, 17, 18, 19, 20]

while True:
	cont = False
	# print(num)
	for i in list_range:
		if num % i != 0:
			num += 2520
			cont = True
	if cont:
		continue
	break

print(num)
print(time.time() - s)
