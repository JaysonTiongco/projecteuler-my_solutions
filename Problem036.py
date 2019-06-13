
# Double-base palindromes

# Problem 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

import time

s = time.time()

# a = bin(585)[2:]

palindromes = []

for i in range(1000000):
	if str(i) == str(i)[::-1] and str(bin(i)[2:]) == str(bin(i)[2:])[::-1]:
		palindromes.append(i)

print(sum(palindromes))
print(time.time()-s)
