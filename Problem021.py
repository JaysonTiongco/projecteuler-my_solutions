# Amicable numbers
# Problem 21 
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import time

s = time.time()

num_1 = 0
num_2 = 0

non_amicable_list = []

total = 0

for i in range(1, 10001):
	sum_divisor = 0
	sum_divisor_2 = 0

	if i in non_amicable_list:
		continue
	
	# FIND THE DIVISORS OF FIRST NUM
	for x in range(1, (i // 2) + 1):
		if i % x == 0:
			sum_divisor += x   # SUM OF PROPER DIVISORS OF FIRST NUM

	if i == sum_divisor:
		non_amicable_list.append(i)
		continue

	# FIND THE DIVISORS OF THE SECOND NUM
	for x in range(1, (sum_divisor // 2) + 1):
		if sum_divisor % x == 0:
			sum_divisor_2 += x

	if i == sum_divisor_2:
		total += i
	else:
		non_amicable_list.append(i)

print(total)
print(time.time() - s)
