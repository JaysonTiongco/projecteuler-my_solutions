# Problem 4 - Largest Palindrome Product
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import time

s = time.time()

num1 = 100
num2 = 100
prod = 0

palindromes = []

while True:
	if num1 >= 1000:
		num1 = 100
		num2 += 1
		# print(str(num2) + '/1000')
	if num2 >= 1000:
		break

	prod = num1 * num2

	if str(prod) == str(prod)[::-1]:
		palindromes.append(prod)

	num1 += 1

palindromes.sort()
print(max(palindromes))
print(time.time() - s)
