import random

a = 1
b = 2

print("a + b = %d" % (a+b))
print("a * b = %d, a / b = %g" % (a*b, a/b))	# %g formats the float in a "logical" way

for i in range(20):		# Range gives back a list(iterator actually...) from 0 to n-1, by default
	print(i)
