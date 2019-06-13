# Digit cancelling fractions

# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
# which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less 
# than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.


import time

s = time.time()


def simplify(n, d):
	n_factors = []
	d_factors = []
	for i in range(2, (n//2)+1):
		if n % i == 0:
			n_factors.append(i)
	else:
		n_factors.append(n)

	for i in range(2, (d//2)+1):
		if d % i == 0:
			d_factors.append(i)
	else:
		d_factors.append(d)

	common_factors = [i for i in n_factors if i in d_factors]
	try:
		gcf = max(common_factors)
	except:
		return
	
	return [n//gcf, d//gcf]


answers = []

for d in range(11, 100):
	if d % 10 == 0:
		continue
	for n in range(11, d):
		if n % 10 == 0:
			continue

		n1 = str(n)[0]
		n2 = str(n)[1]
		d1 = str(d)[0]
		d2 = str(d)[1]

		# if the n and d does not have a common digit
		if not n1 in str(d) and not n2 in str(d):
			continue
		else:
			if n1 == d1:
				c = [n2, d2]
			if n2 == d1:
				c = [n1, d2]
			if n1 == d2:
				c = [n2, d1]
			if n2 == d2:
				c = [n1, d1]

		# print(n,'/',d,' => ',c[0],'/',c[1])

		if (n / d) == (int(c[0]) / int(c[1])):
			answers.append([n, d])


print(answers)

prod_n = 1
prod_d = 1
for i in answers:
	prod_n *= i[0]
	prod_d *= i[1]

print(simplify(prod_n, prod_d))

print(time.time() - s)

# wat, 4/8 not simplified...
# -- a few hours later --
# YEZ SOLVED GUHAHAHAHA
