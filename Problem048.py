"""
Self powers

Problem 48
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""
import time
s = time.time()

def solve(n):
	return n**n

n = input('Enter number: ')
a = [solve(i) for i in range(1, int(n) + 1)]

print(str(sum(a))[-10:])
print(time.time() - s)