#Robert Florance
#Shell Sort w/ Bubble Sort| 12.3.2011 | CP407
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

def shellSort(sortlist):
	
	global counter, swaps
	interval = len(sortlist) // 2 #start with n/2
	while interval > 0:
		
		if sys.argv[2] == 'p': print 'INTERVAL: ', interval 
		for i in range(interval, len(sortlist)):
			val = sortlist[i]
			j = i
			#do bubble sort:
			while j >= interval and sortlist[j-interval] > val:
				#print 'swp: ', sortlist[j], sortlist[j-interval]
				swaps +=1
				counter +=1
				sortlist[j], sortlist[j-interval] = sortlist[j-interval], sortlist[j]	
				j -= interval
		interval //= 2 #now n/4 .. 1
	return sortlist

for i in range(20):

	#shuffle the list we are working with
	random.shuffle(sortlist)

	#time the algorithm
	t0 = time.clock()
	result = shellSort(sortlist)
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
	writer = csv.writer(open('ssb.csv','a'))
	writer.writerows([ (entries, counter, timer, swaps) ])

