import sys

def nameMult(name, num):
	name = num*name		# Gives back the string num times

	return name

_, name, num = sys.argv
num = int(num)

print(nameMult(name, num))
