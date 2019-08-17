"""
Permuted multiples

Problem 52
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

import time


class Problem52:
	def main(self):
		counter = 1
		while True:
			counter += 1
			if self.perm_multiples(counter):
				return counter


	def perm_multiples(self, n: int) -> bool:
		nums = [n*j for j in range(2, 7)]
		return all(self.permutation(str(num), str(n)) for num in nums)


	def permutation(self, s1: str, s2: str) -> bool:
		s2 = [i for i in s2]
		for i in s1:
			if i not in s2: return False
			s2.remove(i)
		return True if len(s2) == 0 else False


if __name__ == '__main__':
	instance = Problem52()
	start = time.time()

	result = instance.main()

	duration = time.time() - start
	print(result, duration)


# huge improvement in code.. solved 8/17/2019 - 8:40pm (GMT +8)
