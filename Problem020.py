# Factorial digit sum
# Problem 20 
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import time

s = time.time()

num = 1
sumtotal = 0

for i in range(2, 101):
	num = num * i

for i in str(num):
	sumtotal += int(i)

print(sumtotal)
print(time.time() - s)
