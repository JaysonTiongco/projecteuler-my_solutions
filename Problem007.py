# Problem 7 - 10 001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from timer import timed
import math


@timed
def problem_007() -> int:
	counter = 0
	num = 1

	while True:
		num += 1
		for i in range(2, int(math.sqrt(num)) + 1):
			if (num % i) == 0:
				break
		else:
			counter += 1
			if counter == 1001:
				return num


if __name__ == '__main__':
	print(f"answer: {problem_007()}")
