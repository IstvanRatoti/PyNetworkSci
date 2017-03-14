import sys, random

# Read arguments.

_, nodes, edges = sys.argv

# Convert them to integer.
nodes = int(nodes); edges = int(edges)

# node2comp[i] is the component index of node i.
node2comp = [_ for _ in range(nodes)]

# comp2nodelist[i] is the list of nodes of component i.
comp2nodelist = {n:[n] for n in range(nodes)}

# node2neiset[i] is the set of neighbors of node i
node2neiset = {}

# We assume that p = 2e/n^2 << 1, <k> = 2e/n.
# enow us the current number of links in the network
while enow < edges:
	# Try to insert new link -> make sure A and B are not yet connected.
		# Select new link -> select A!=B node.

	# If A and B belong to different components, 
		# 3 steps: update component index book-keeping.

	# Insert edge to the network.
