col = ["green", "blue", "yellow", "black", "blue"]

print(col[-2])		# Counts from the back, should print "black".
print(col[1:4])		# Slicing.
print(col[0:-2])	# Sliced from 0 to 3 !!!
print(col[0:-1:2])	# Slicing is "from : to : leap length".

str = "Hello, World!"

print(str[1:-1:3])

print(col)
print(col.pop())	# Pop last element.
print(col)
print(col.pop(-2))	# Pop the 2nd element from the back.
print(col)
