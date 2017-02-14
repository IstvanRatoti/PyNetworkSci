import sys

_, infile = sys.argv	# Underscore discards the first variable here!

with open(infile, "r") as f:
	name = f.readline().rstrip()
	print("Hello, %s!" % name)
