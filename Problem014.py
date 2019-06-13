# Longest Collatz sequence
# Problem 14 
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

s = time.time()

num = 999999
temp = 0

seq_count = 0
highest = 0
num_of_highest = 0

# method if even
def if_even(num):
	return int(num/2)

# method if odd
def if_odd(num):
	return int((num * 3) + 1)

while True:
	temp = num

	while True:
		if temp % 2 == 0:
			temp = if_even(temp)
		else:
			temp = if_odd(temp)
		seq_count += 1
		if temp == 1:
			break

	if num == 1:
		break

	if seq_count > highest:
		highest = seq_count
		num_of_highest = num

	# print(str(num) + ": " + str(seq_count))
	num -= 1
	seq_count = 0

print("Highest: " + str(highest) + " Num: " + str(num_of_highest))
print(time.time() - s)

# SOLVED 6 MINUTES.......... need improvement
