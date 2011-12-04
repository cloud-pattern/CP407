#Robert Florance
#Merge Sort| 11.20.2011 | CP407
import math, time, sys, csv, random
from decimal import Decimal

datafile = sys.argv[1]
counter = 0
swaps = 0
timer = 0
f = open(datafile)
sortlist = f.readlines()
sortlist = map(lambda s: int(s.strip()), sortlist)
entries = len(sortlist)

def merge(left, right):
	global counter
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		counter +=1
		if left[i] <= right[j]:
			result.append(left[i])
			i +=1
		else:
			result.append(right[j])
			j +=1

	result += left[i:]
	result += right[j:]
	return result

def mergeSort(sortlist):
	global counter
	if len(sortlist) < 2:
		return sortlist
	else:
		middle = len(sortlist)/2
		left = mergeSort(sortlist[:middle])
		right = mergeSort(sortlist[middle:])
		return merge(left, right)

for i in range(20):	

	#shuffle the list we are working with
	random.shuffle(sortlist)

	#time the algorithm
	t0 = time.clock()
	result = mergeSort(sortlist) 
	timer += time.clock() - t0

# take averages
counter = math.floor(counter/20)
swaps = math.floor(swaps/20)
timer = timer/20
timer =  Decimal(timer).quantize(Decimal('0.000000000'))

#print results
if sys.argv[2] == 'p': print result
print entries, "entries in list"
print counter, "steps"
print timer, "timer process time" 
print swaps, "swaps"

#record result
if sys.argv[2] == 'r':
	writer = csv.writer(open('ms.csv','a'))
	writer.writerows([ (entries, counter, timer) ])
