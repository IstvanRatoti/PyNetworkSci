import random
import sys

def generate(max):		# This function generates the random numbers and calculates
	list = []			# the mean and the median, and returns it.
	sum = 0
	
	for i in range(max):				# Generates the random numbers and stores them in a list
		list.append(random.random())	# and the sum.
		sum += list[i]
	
	list.sort()				# Sorts the list for the calculation of the median.
	
	if int(max)%2 == 0:		# Median for an even number of elements.
		median = (list[int(int(max)/2)] + list[int(int(max)/2 - 1)]) / 2
	else:					# And for odd.
		median = list[int(int(max)/2)]
	
	mean = sum/float(max)	# Calculates the mean.
	#print("\t%0.4g\t\t%0.4g" % (mean, median))	Test code
	return (mean, median)


def makegroup(max):		# This functions makes the 10 groups and calculates
	minmean = 1.0		# the ranges of the means and medians.
	maxmean = 0.0
	minmedian = 1.0		# The initial min and max values are definately
	maxmedian = 0.0		# smaller/bigger than anything we expect.
	
	for i in range(10):
		mean, median = generate(max)
		
		if mean < minmean:		# Check for the smallest mean.
			minmean = mean
		if mean > maxmean:		# The largest mean.
			maxmean = mean
		
		if median < minmedian:	# Same deal with medians as above.
			minmedian = median
		if median > maxmedian:
			maxmedian = median;
	
	meanrange = maxmean - minmean
	medianrange = maxmedian - minmedian
	#print("Range:\t%0.4g\t\t%0.4g" %(meanrange, medianrange))	Test code
	return (meanrange, medianrange)


print("Elements\tMean range\tMedian range")
for num in (10,30,100,300,1000,3000,10000, 30000, 100000, 300000, 1000000, 3000000, 10000000):
	meanrange, medianrange = makegroup(num)
	
	print("%8d\t\t%0.4g\t\t%0.4g" % (int(num), meanrange, medianrange))
