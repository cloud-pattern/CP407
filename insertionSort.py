#Robert Florance
#Insertion Sort | 117.2011 | CP407
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

def insertionSort(srtlst, entries):
	global swaps, counter
	for j in range(0, entries):
		key = srtlst[j]
		i = j - 1
		while (i >= 0 and srtlst[i] > key):
			counter+=1
			swaps+=1
			srtlst[i + 1] = srtlst[i]	
			i-=1
		srtlst[i + 1] = key
		swaps+=1
	return srtlst


for i in range(20):	

	#shuffle the list we are working with
	random.shuffle(sortlist)

	#time the algorithm
	t0 = time.clock()
	result = insertionSort(sortlist, entries) 
	timer += time.clock() - t0

# take averages
counter = math.floor(counter/20)
swaps = math.floor(swaps/20)
timer = timer/20
timer =  Decimal(timer).quantize(Decimal('0.000000000'))


#print results
if sys.argv[2] == 'p': print result
print entries, "entries in list"
print counter, "avg steps"
print timer, "avg. time" 
print swaps, "avg. swaps"

#record result
if sys.argv[2] == 'r':
	writer = csv.writer(open('is.csv','a'))
	writer.writerows([ (entries, counter, timer, swaps) ])
