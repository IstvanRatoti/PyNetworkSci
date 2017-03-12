import sys

# This function adds a link between 2 substrings. If they did not exist, it creates
# the entry.
def addlink(key1, key2, dict):
	if key1 not in dict:	# Create entry if it didn't exist.
		dict[key1] = 0
	dict[key1] += 1		# Increment it.
	
	if key2 not in dict:	# Same as above.
		dict[key2] = 0
	dict[key2] += 1

# This function creates and returns dictionary of all the 3 character substring and their
# number of links to other substrings. 
def get3chardict(filename):
	dict = {}
	
	# Open the file.
	with open(filename, "r") as file:
		
		str = file.read()	# Read the whole file. Not very resource efficient...
		#print(str)	# Debug code.
		
		# Start the loop on the third character, and finish it 3 characters before the
		# end of the string.
		for n in range(3,len(str)-2):
			substr1 = str[n:n+3]	# Get the 3 char long substring starting at n.
			substr2 = str[n-3:n]	# And the one right in front of it.
			addlink(substr1, substr2, dict)		# Add a link to the two adjacent substrings.
			#print("Adding link between: \"%s\"\t\"%s\"" %(substr2, substr1))	# Debug code.
	
	return dict

# Creates a probability density function from the 3 character substring dictionary.
def createpdf(values):
	h = {}
	
	# This loop creates a histogram that we need for the pdf.
	# The code inside the loop is pretty similar to the addlink function.
	for n in values:
		if n not in h:
			h[n] = 0
		h[n] += 1
	
	#print(h)	# Debug code.
	#print(len(values))	# Debug code.
	
	# Same compact code as found in pdf.py. For details on what and how it does, refer
	# to that file.
	return {int(_):1.0*h[_]/len(values) for _ in h}

# Creates the complementary cumulated density function from the pdf, and returns it.
def createccdf(pdf):
	ccdf = {}
	
	# We need a list of the keys, so we can sort it.
	keylist = list(pdf.keys())
	keylist.sort()
	#print(keylist)	# Debug code.
	
	# The outer loop, sets our ccdf dictionary. Runs until it reaches the largest key.
	for value in range(1,max(keylist)):
		sum = 0
		
		# Inner loop, sums up the pdf values up to our current limit.
		for key in keylist:
			if value <= key:
				break
			
			sum += pdf[key]
		
		#print(sum)	# Debug code.
		ccdf[value] = 1 - sum
	
	return ccdf

# Usual argument number check.
if 3 != len(sys.argv):
	print("The program expects only one argument!")
	exit(1)

_, infile, outfile = sys.argv

dict = get3chardict(infile)
#print(dict)	# Debug code.

pdf = createpdf(dict.values())
#print(pdf)	# Debug code.

ccdf = createccdf(pdf)

# Simply writes the data to the specified output file.
with open(outfile, "w") as file:
	for key in ccdf:
		file.write("%d\t%g\n" % (key, ccdf.get(key)))
