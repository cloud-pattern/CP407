#Robert Florance
#Recursive Binary Search | 11.2.2011 | CP407
import math, time, sys, csv, random
from decimal import Decimal

search = 11111 #all lists have numbers <= 9999, so this will not be on any list 
datafile = sys.argv[1]
counter = 0
f = open(datafile)
searchlist = f.readlines()
searchlist = map(lambda s: int(s.strip()), searchlist)
entries = len(searchlist)
lo, hi = 0, entries

def binarySearchRecursive(low, high):
	global searchlist
	global counter
	if low > high:
		return False
	else:
		mid = int(math.floor((low + high)/2))
		counter+=2
		if search == searchlist[mid-1]:
			counter-=1
			return True
		elif search < searchlist[mid-1]:
			binarySearchRecursive(low, mid -1)
		else:
			binarySearchRecursive(mid +1, high)

#time the algorithm
t0 = time.clock()
result = binarySearchRecursive(lo, hi) 
timer = time.clock() - t0

timer =  Decimal(timer).quantize(Decimal('0.000000000'))

#print results
print result, "(on list?)"
print entries, "entries in list"
print counter, "steps"
print timer, "seconds process time"

#record results
if sys.argv[2] == 'r':
	writer = csv.writer(open('bsr.csv','a'))
	writer.writerows([ (entries, counter, timer) ])
