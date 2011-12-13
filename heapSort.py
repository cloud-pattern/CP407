#Robert Florance
#Heap Sort| 11.9.2011 | CP407
import math, time, sys, csv, random
from decimal import Decimal

datafile = sys.argv[1]
counter = 0
swaps = 0
timer = 0
f = open(datafile)
sortlist = f.readlines()
array = map(lambda s: int(s.strip()), sortlist)
entries = len(array)

def Parent(i): return math.floor(i/2)
def lChild(i): return 2*i -1
def rChild(i): return 2*i 

def siftDown(loc, length):
	global array
	left = lChild(loc)
	right = rChild(loc)
	print array	
	print 'sifting on parent', loc,'(', array[loc],')'
	print 'its children are ', array[left], array[right] 

	if left <= length and array[left] > array[loc]:
		largest = left
	else:
		largest = loc

	if right <= length and array[right] > array[largest]:
		largest = right
	
	if largest != loc:
		array[loc], array[largest] = array[largest], array[loc]
		siftDown(largest, length)

def makeHeap():
	global array
	length = len(array)
	for loc in range(int(math.floor(length/2)), 0, -1):
		siftDown(loc, length-1)

def sortHeap():
	global array
	makeHeap()
	length = len(array)
	for i in range(length, 0, -1):
		array[1], array[i] = array[i], array[1]
		length -=1
		siftDown(0, length) 


#shuffle the list we are working with
random.shuffle(array)

#time the algorithm
t0 = time.clock()
sortHeap() 
timer += time.clock() - t0
