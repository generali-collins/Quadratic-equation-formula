#Collins Wanga
# Python program for solving a quadratic equation.

from math import sqrt
try:	

	a = 1
	b = 2
	c = 1
	i = b**2-4 * a * c

	
	d = sqrt(-i)
	try:
		z = sqrt(i)
		# two resultants
		e = (-b + d) / 2 * a
		f = (-b-d) / 2 * a
		if e == f:
			print("The values for x is " + str(e))
		else:
			print("The value for x1 is " + str(e) +
				" and x2 is " + str(f))
	except ValueError:
		print("The result for your equation is in complex")
		

		print("x1 = " + str(-b) + "+" + str(g) + "i/" + str(2 * a) +
			" and x2 = " + str(-b) + "-" + str(g) + "i/" +
			str(2 * a))
		
except ValueError:
	print("Enter a number")
