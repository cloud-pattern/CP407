#Robert Florance
#Exchange Sort| 11.4.2011 | CP407
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

def exchangeSort(srtlst, entries):
	global counter, swaps
	for i in range(entries):
		for j in range(i+1, entries):
			counter+=1
			if srtlst[j] < srtlst[i]:
				srtlst[j], srtlst[i] = srtlst[i], srtlst[j]
				swaps+=1
	return srtlst

for i in range(20):	

	#shuffle the list we are working with
	random.shuffle(sortlist)

	#time the algorithm
	t0 = time.clock()
	result = exchangeSort(sortlist, entries) 
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
	writer = csv.writer(open('es.csv','a'))
	writer.writerows([ (entries, counter, timer, swaps) ])
