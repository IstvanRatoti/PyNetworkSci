import sys

def addpair(pair, chromomap):	# Increments the corresponding pair
	if 'AA' == pair:			# to the dictionary.
		chromomap['AA'] += 1
	elif 'TT' == pair:
		chromomap['TT'] += 1
	elif 'CC' == pair:
		chromomap['CC'] += 1
	elif 'GG' == pair:
		chromomap['GG'] += 1
	elif ('CG' == pair) or ('GC' == pair):
		chromomap['CG'] += 1
	elif ('AT' == pair) or ('TA' == pair):
		chromomap['AT'] += 1
	elif ('AC' == pair) or ('CA' == pair):
		chromomap['AC'] += 1
	elif ('AG' == pair) or ('GA' == pair):
		chromomap['AG'] += 1
	elif ('TC' == pair) or ('CT' == pair):
		chromomap['TC'] += 1
	elif ('TG' == pair) or ('GT' == pair):
		chromomap['TG'] += 1
	else:
		print('Wrong pair: %s' % pair)

if 3 != len(sys.argv):		# Exit if wrong number of arguments are given.
	print('Error! an input file and an output file!')
	sys.exit(1)

_, infile, outfile = sys.argv

file = open(infile, 'r')

pair = ''
chromomap = {'AA':0, 'TT':0, 'CC':0, 'GG':0, 'CG':0, 'AT':0, 'AC':0, 'AG':0, 'TC':0, 'TG':0}

file.seek(200)	# Skip the first 200 bytes, containing N-s and the first comment line.
while True:
	char = file.read(1)
	#print(char, end='')
	
	if 0 == len(char):		# DIY do...while loop.
		break
	elif 'N' == char:		# N-s are not important to us.
		if 0 != len(pair):
			pair = ''		# Reset the pair on an N.
		continue
	elif '\n' == char:		# Neither are newline characters.
		continue
	elif  0 == len(pair):	# If we have an empty pair string,
		pair = char			# this char will be the first.
		continue
	else:
		pair += char		# Add a second char.
		if 3 == len(pair):		# If we already had 2 chars
			pair = pair[1:]		# delete the other one.
		
		#print(pair, end=' ')	#debug code
		addpair(pair, chromomap)

file.close()

for key, value in chromomap.items():	# Debug code to check the file contents.
		print('%s: %d' % (key, value))

with open(outfile, 'w') as f:
	for key, value in chromomap.items():
		f.write('%s: %d\n' % (key, value))
