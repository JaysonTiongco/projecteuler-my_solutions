"""
Prime permutations

Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import math, time

s = time.time()

def equal_diff(n1: int, n2: int, n3: int) -> bool:
	li = [n1, n2, n3]
	li.sort()
	if li[2]-li[1] == li[1]-li[0]:
		return True
	return False

def permutation(n1: int, n2: int, n3: int) -> bool:
	n1, n2, n3 = list(str(n1)), list(str(n2)), list(str(n3))
	if len(n1) != len(n2) or len(n2) != len(n3):
		return False
	n1.sort()
	n2.sort()
	n3.sort()
	if n1 == n2 and n2 == n3:
		return True
	return False
	
def is_prime(n: int) -> bool:
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True
	
li = []
for n in range(1000, 10000):
	if is_prime(n):
		if len(str(n)) == 4:
			li.append(n)

p1, p2 = 0, 1
countdown = 2 # only two sets of these numbers exists

for p1 in range(0, len(li)-2):
	for p2 in range(p1+1, len(li)-1):
		dif = li[p2] - li[p1]
		if li[p2] + dif in li:
			n1, n2, n3 = li[p1], li[p2], li[p2]+dif
			if permutation(n1, n2, n3):
				countdown -= 1
				print("{} = {} + {} + {}, {}-{}={} {}-{}={}  ANS: {}{}{}".format(
					n1+n2+n3,
					n1, n2, n3,
					n2, n1, n2-n1,
					n3, n2, n3-n2,
					n1, n2, n3
					)
				)
			if countdown == 0: break

print(time.time() - s)
