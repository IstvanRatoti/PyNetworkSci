import random

array = []	# 1
sum = 0

for _ in range(100):	# 2
	num = random.random()
	array.append(num)	# 3
	sum += num

avg = sum/len(array)
array.sort(key=float)	# Tell it to sort it as float.
med = array[len(array)//2]

print("Average: %g\tMedian: %g" % (avg, med))

# arr = [random.random() for _ in range(100)]	 Combination of 1, 2 and 3. Not applicable here
# because we need every single element for the sum. Alternatively, we can use the sum() function
# on our list.
