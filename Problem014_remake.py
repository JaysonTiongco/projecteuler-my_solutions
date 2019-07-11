"""
Longest Collatz sequence
Problem 14 
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting 
numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time

s = time.time()


def if_even(num):
	return int(num/2)


def if_odd(num):
	return int((num * 3) + 1)


highest_sequence_num = 0
highest_sequence_count = 0

for n in range(13, 1000000):
	store_n_value = n
	sequence_count = 1
	while not n == 1:
		sequence_count += 1
		if n % 2 == 0:
			n = if_even(n)
		else:
			n = if_odd(n)
	if sequence_count > highest_sequence_count:
		highest_sequence_count = sequence_count
		highest_sequence_num = store_n_value


print("{} with a sequence count of {}.".format(highest_sequence_num, highest_sequence_count))
print(time.time() - s)

"""
Looks better
Works better.. NOT
still slow..
"""
