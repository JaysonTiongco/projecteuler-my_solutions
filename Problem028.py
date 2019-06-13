# Number spiral diagonals

# Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import time

s =  time.time()

total_x, total_y = 1001, 1001

x = (total_x // 2)
y = (total_y // 2)

diagonal_numbers = []

right = True
down = False
left = False
up = False

grid = [[" " for i in range(total_x)] for i in range(total_y)]

for n in range(total_x**2):
	n += 1

	# print(str(n)+" = "+str(y)+","+str(x))

	grid[y][x] = n

	if n == total_x**2:
		continue

	if right:
		x += 1
		if grid[y+1][x] == " ":
			right = False
			down = True

	elif down:
		y += 1
		if grid[y][x-1] == " ":
			down = False
			left = True

	elif left:
		x -= 1
		if grid[y-1][x] == " ":
			left = False
			up = True

	elif up:
		y -= 1
		if grid[y][x+1] == " ":
			up = False
			right = True


x = (total_x // 2)
y = (total_y // 2)

len_from_center = x

diagonal_numbers.append(grid[y][x])


# upper left diagonal
for i in range(len_from_center):
	y -= 1
	x -= 1
	diagonal_numbers.append(grid[y][x])
	print(str(y) + "," + str(x))


# upper right diagonal
x = (total_x // 2)
y = (total_y // 2)
for i in range(len_from_center):
	y -= 1
	x += 1
	diagonal_numbers.append(grid[y][x])
	print(str(y) + "," + str(x))


# lower left diagonal
x = (total_x // 2)
y = (total_y // 2)
for i in range(len_from_center):
	y += 1
	x -= 1
	diagonal_numbers.append(grid[y][x])
	print(str(y) + "," + str(x))


# lower right diagonal
x = (total_x // 2)
y = (total_y // 2)
for i in range(len_from_center):
	y += 1
	x += 1
	diagonal_numbers.append(grid[y][x])
	print(str(y) + "," + str(x))

diagonal_numbers.sort()

print("total: " + str(sum(diagonal_numbers)))

print(time.time() - s)
