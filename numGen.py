#Generate random numbers for sorting lists
import random, sys

many = int(sys.argv[1])
where = sys.argv[2]

f = open(where, 'a')
for i in range(many):
	n = str(random.randint(0,10000))
	f.write(n+'\n')
