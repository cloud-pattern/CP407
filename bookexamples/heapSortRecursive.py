#Robert Florance
#Heap Sort| 11.9.2011 | CP407
import math, time, sys, csv, random
from decimal import Decimal

REPEAT = 20
datafile = sys.argv[1]
counter = 0
swaps = 0
timer = 0
f = open(datafile)
sortlist = f.readlines()
array = map(lambda s: int(s.strip()), sortlist)
heapSize = len(array) -1 #THIS REPRESENTS THE INDEX OF THE LAST NODE
length = len(array)

def siftDown(index):
	
	global array, heapSize, counter
	siftkey = array[index]
	parent = index
	spotfound = False
	while (2*parent +1 <= heapSize and spotfound == False):
		counter +=2
		if (2*parent +1 < heapSize and array[2*parent +1] < array[2*parent +2]):
			largerchild = 2*parent +2
		else:
			largerchild = 2*parent +1
		if siftkey < array[largerchild]:
			array[parent] = array[largerchild]
			parent = largerchild
		else:
			spotfound = True
	array[parent] = siftkey 

def root():
	global array, heapSize
	keyout = array[0]
	array[0] = array[heapSize]
	heapSize -=1
	siftDown(0) #sift down the root, which we pulled from the bottom
	return keyout

def removeKeys():
	global array, length
	for i in range(length -1, 0, -1): #CHECK INDEX
		array[i] = root()

def makeHeap():
	global heapSize
	for i in range(int((math.ceil(heapSize/2) -1)), -1, -1):
		siftDown(i)

for i in range(REPEAT):	
	#shuffle the list we are working with
	random.shuffle(array)
	#reset heap size
	heapSize = len(array) -1
	if sys.argv[2] == 'p': print 'start: ', array
	#time the algorithm
	t0 = time.clock()
	makeHeap() 
	removeKeys()
	timer += time.clock() - t0
	if sys.argv[2] == 'p': print 'end: ', array

# take averages
counter = math.floor(counter/REPEAT)
swaps = math.floor(swaps/REPEAT)
timer = timer/REPEAT
timer =  Decimal(timer).quantize(Decimal('0.000000000'))

#print results
print "averages for running ", REPEAT, " times"
print length, "entries in list"
print counter, "steps"
print timer, "timer process time" 
print swaps, "swaps"

#record result
if sys.argv[2] == 'r':
	writer = csv.writer(open('hsi.csv','a'))
	writer.writerows([ (entries, counter, timer, swaps) ])
