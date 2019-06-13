# Problem 9 - Special Pythagorean Triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#  a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time

s = time.time()

_ans = []

def checker(num1, num2, num3):
	if (num1**2 + num2**2) == num3**2:
		_ans.append(num1)
		_ans.append(num2)
		_ans.append(num3)
		# print('*****FOUND****** ' + str(num1) + ' ' + str(num2) + ' ' + str(num3))


for a in range(0, 1001):
	for b in range(a + 1, 1001):
		c = 1000 - (a + b)
		if (c <= b):
			continue
		if a + b + c == 1000:
			checker(a, b, c)
			# print(str(a) + ' ' + str(b) + ' ' + str(c))

print(_ans)

print(_ans[0] * _ans[1] * _ans[2])
print(time.time() - s)
