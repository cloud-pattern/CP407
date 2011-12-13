#Robert Florance
#Quick Sort| 11.4.2011 | CP407
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

def quickSort(low, high):
	global sortlist, counter
	#counter+=1
	if high > low:
		pivot = partition(low, high)
		quickSort(low, pivot)
		quickSort(pivot +1, high)
	return sortlist

def partition(low, high):
	global sortlist, counter, swaps
	pivot_item = sortlist[low]
	j = low
	for i in range(low +1, high):
		counter+=1
		if sortlist[i] < pivot_item:
			j+=1
			swaps +=1
			sortlist[i], sortlist[j] = sortlist[j], sortlist[i]
	pivot = j
	swaps +=1
	sortlist[low], sortlist[pivot] = sortlist[pivot], sortlist[low]
	return pivot

for i in range(20):	

	#shuffle the list we are working with
	random.shuffle(sortlist)

	#time the algorithm
	t0 = time.clock()
	result = quickSort(0, entries) 
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
print timer, "seconds process time" 
print swaps, "swaps"

#record result
if sys.argv[2] == 'r':
	writer = csv.writer(open('qs.csv','a'))
	writer.writerows([ (entries, counter, timer, swaps) ])
