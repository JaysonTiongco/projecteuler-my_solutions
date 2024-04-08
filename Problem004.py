# Problem 4 - Largest Palindrome Product
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from timer import timed


@timed
def problem_004() -> int:
    palindromes = []

    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j

            # Check if palindrome
            if str(product) == str(product)[::-1]:
                palindromes.append(product)

    return max(palindromes)


if __name__ == '__main__':
    print(f"answer: {problem_004()}")
