import sys

_, infile = sys.argv

with open(infile, 'r') as file:
	#mystr = file.read()	# Reads the entire file.
	myset = set()	# Need to declare the set here. (visibility)

	#for char in mystr:
	#	myset.add(char)
	[myset.add(char) for char in file.read()]	# Compressed type of commented out lines
	print(myset)
