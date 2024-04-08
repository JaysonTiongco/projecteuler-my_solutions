# Problem 6 - Sum Square Difference
#
# The sum of the squares of the first ten natural numbers is,
#			1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#			(1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
# 			3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

from timer import timed


@timed
def problem_006() -> int:
    total_sumsquare = sum([i**2 for i in range(1, 101)])
    total_squaresum = sum([i for i in range(1, 101)]) ** 2
    return total_squaresum - total_sumsquare


if __name__ == '__main__':
    print(f"answer: {problem_006()}")
