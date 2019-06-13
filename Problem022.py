# Names scores
# Problem 22 
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value 
# by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
# name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import time
import csv

s = time.time()

name_list = []

name_points = 0
total_points = 0
file = "Problem022_names.txt"

with open(file) as dataset:
	data = csv.reader(dataset, delimiter=",")

	for i in data:
		for item in i:
			name_list.append(item)

sorted_list = sorted(name_list)

for name in sorted_list:
	name_points = 0
	for char in name:
		name_points += ord(char.lower()) - 96
	name_points *= (sorted_list.index(name) + 1)
	total_points += name_points

print(total_points)
print(time.time() - s)
