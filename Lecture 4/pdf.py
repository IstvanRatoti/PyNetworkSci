# Histogram and pdf of the occurance number of a character.
import sys

def file2charhist(infile, dict):
	# Open file for reading.
	with open(infile, "r") as file:
		for char in file.read():
			#print(char)	# Debug code.
			# If we already have a key corresponding to
			# this character, just increment it.
			if char in dict:
				dict[char] += 1
			else:	# If we dont, create it.
				dict[char] = 1
	
	#print(h)	# Debug code.

def list2pdf(list):
	# Count number of occurances from list.
	# h[n] is the number of times that "n" appears in list.
	# Assumption: h.values() are integers.
	h = {}
	
	for n in list:
		# If we have not yet seen n.
		if n not in h:
			# Set the usage number to 0
			h[n] = 0
		
		# In all cases, increment h[n].
		h[n] += 1
	
	#print(h)	# Debug code
	pdf = {}
	
	return{int(_):1.0*h[_]/len(list) for _ in h}

scriptfile, outfile = sys.argv

# h[a] is the number of times the "a" character in the
# input file.
h = {}

file2charhist(scriptfile, h)

# pdf[n] is the probability of the occurance of a
# character n times.
pdf = list2pdf(h.values())

# Print output.
print(pdf)
