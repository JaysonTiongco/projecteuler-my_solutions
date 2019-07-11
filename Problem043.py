"""
Sub-string divisibility

Problem 43
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of 
the digits 0 to 9 in some order, but it also has a rather interesting sub-string
divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations
import time


s = time.time()
num = 1234567890


def tuple_to_int(t):
	s = ''
	for i in t:
		s += str(i)
	return int(s)


def check(num):
	num = str(num)
	odd_num = [2, 3, 5, 7, 11, 13, 17]
	for i in range(1, 8):
		try:
			n = int(num[i]+num[i+1]+num[i+2]) # + concatenation is fastest
		except:
			pass # error on  n = int(num[i]+num[i+1]+num[i+2])  i+2 index error, just sayin' yo
		if not n % odd_num[i-1] == 0:
			return False
	return True


_sum = 0
for i in permutations(str(num)):
	if i[0] == 0:
		continue
	n = tuple_to_int(i)
	if check(n):
		_sum += n
		print(n)


print(_sum)
print(time.time() - s)

# SOLVED JULY-11-2019 around 8:30 pm
# took almost 2 minutes tho... need to improve code/algo
