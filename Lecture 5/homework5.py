import sys, random

# Creates a probability density function.
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

if 4 != len(sys.argv):
	print("Illegal number of arguments! Need to specify node and edge number and the output file!")
	exit(1)

_, nodes, edges, outfile = sys.argv

# Convert them to integer.
nodes = int(nodes); edges = int(edges)

# node2neiset[i] is the dictionary of the neighbors of node i.
node2neidict = {}

# Edges currently in the network.
enow = 0

while enow<edges:
	n1 = random.randint(0, nodes-1)		# Generate the first node to connect...
	n2 = random.randint(0, nodes-1)		# with the second node.
	
	if n1 == n2:	# Don't connect the node with itself
		continue
	
	if n1 not in node2neidict:		# Check if n1 is in dictionary.
		node2neidict[n1] = set()
	if n2 not in node2neidict:		# Check if n2 is in dictionary.
		node2neidict[n2] = set()
	
	# Add neighbor to both sets and increment present edge numbers.
	if n2 not in node2neidict[n1]:
		node2neidict[n1].add(n2)
		node2neidict[n2].add(n1)
		enow+=1

#for k, v in node2neidict.items():	# Debug code
#	print("Node %d:" % k, end=' ')
#	print(v, end=' ')
#	print(len(v))

# Create node degrees from the node2neidict sets.
nodedegrees = [len(value) for value in node2neidict.values()]
#print(nodedegrees)	# Debug code.

# Create pdf from nodedegrees.
pdf = createpdf(nodedegrees)
#print(pdf)	# Debug code.

# Create the ccdf from the pdf.
ccdf = createccdf(pdf)
#print(ccdf)	# Debug code.

# Simply writes the data to the specified output file.
with open(outfile, "w") as file:
	for key in ccdf:
		file.write("%d\t%g\n" % (key, ccdf.get(key)))