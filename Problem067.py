# Maximum path sum II
# Problem 67 
# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
 # the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
 # a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem,
 # as there are 299 altogether! If you could check one trillion (1012) routes every second
 # it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

import time

s = time.time()


def check_higher_sum(num1, num2, num_above):
	sum1 = int(num1) + int(num_above)
	sum2 = int(num2) + int(num_above)
	if sum1 > sum2:
		return sum1
	else:
		return sum2
		

file = "Problem067_triangle.txt"
triangle = ""

with open(file) as outfile:
	for i in outfile:
		triangle += i

_arr = triangle.split("\n")
del _arr[len(_arr) - 1]

data = []
for i in _arr:
	data.append(i.split())

for x in range(len(data) - 1, 0, -1):
	line = data[x]
	line_above = data[x - 1]
	for i in range(0, len(line) - 1):
		line_above[i] = check_higher_sum(line[i], line[i+1], line_above[i])

print(data[0])
print(time.time() - s)
