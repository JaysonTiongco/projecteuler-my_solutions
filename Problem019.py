# Counting Sundays
# Problem 19 
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September, April, June and November.
# All the rest have thirty-one, Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import time

s = time.time()


def leap_year(y):
	if y % 100 == 0:
		#no leapyear unless divisible by 400
		if y % 400 == 0:
			return True
		else:
			return False
	else:
		if y % 4 == 0:
			return True
		else:
			return False


days = ['Monday   ', 'Tuesday  ', 'Wednesday', 'Thursday ', 'Friday   ', 'Saturday ', 'Sunday   ']

# day 1 = monday, upto day 7
_day = 1
dd = 1
mm = 1
yy = 1900

counter = 0

# show every date since 1900
# print(days[0],': ',str(dd),':',str(mm),':',str(yy))

while yy != 2001:
	dd += 1

	_day += 1
	if _day >= 8:
		_day = 1

	if (mm == 2) and (dd == 29):
		if not leap_year(yy):
			dd = 1
			mm += 1

	if (mm == 2) and (dd == 30):
		if leap_year(yy):
			dd = 1
			mm += 1

	if dd >= 31:
		if (mm == 4) or (mm == 6) or (mm == 9) or (mm == 11):
			dd = 1
			mm += 1
		elif (mm != 2) and (dd == 32):
			dd = 1
			mm += 1

	if mm == 13:
		mm = 1
		yy += 1

	if (yy >= 1901) and (yy <= 2000):
		if (dd == 1) and (_day == 7):
			counter += 1

	# show every date since 1900
	# print(days[_day-1],': ',str(dd),':',str(mm),':',str(yy))

print(counter)
print(time.time()-s)

# SOLVED JUNE/8/2019 NOICE!
# calculated in less than a second NOICE~!
