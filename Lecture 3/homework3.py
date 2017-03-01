import sys

def readdata(file):		# Reads the data into a list.
	list = []
	count = 0		# For debugging.
	
	str = file.readline()	# Read the first line.
	while '' != str:	# Stop loop if end of file is reached.
		list.append(int(str[439:447]))
		count += 1
		str = file.readline()
	
	return (list, count)

def valuesover(value, list):	# Counts the number of properties over the given value.
	count = 0
	
	for item in list:
		if value >= item:	# Stop the loop if we go over the value in our sorted list.
			break
		count += 1
		
	return count

_, infile, outfile = sys.argv

if 3 != len(sys.argv):	# Simple argument checker.
	print('Wrong number of arguments!')
	sys.exit(1)

list = []

with open(infile, 'r') as file:
	list, count = readdata(file)

#print('Reading done!\nLines read: %d\tSize of list: %d' % (count, len(list)))	Test code

list.sort(reverse=True)

#print('Value\t\tNumber')	Test code
with open(outfile, 'w') as file:
	for value in range(0,100000000,1000):
		file.write('%9d\t%d\n' % (value, valuesover(value, list)))
