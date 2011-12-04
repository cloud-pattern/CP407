from collections import defaultdict
from heapq import *

def prim( nodes, edges ):
    conn = defaultdict( list )
    for n1,n2,c in edges:
        conn[ n1 ].append( (c, n1, n2) )
        conn[ n2 ].append( (c, n2, n1) )

    print 'conn list', conn

    mst = []
    used = set( nodes[ 0 ] )
    print 'used list', used
    usable_edges = conn[ nodes[0] ][:]
    print 'usable_edges list', usable_edges
    heapify( usable_edges )

    while usable_edges:
        cost, n1, n2 = heappop( usable_edges ) #grab the smallest of connected edges
        if n2 not in used:
            used.add( n2 )
            mst.append( ( n1, n2, cost ) )

            for e in conn[ n2 ]:
                if e[ 2 ] not in used:
                    heappush( usable_edges, e ) #add the edges that we are now connected to
    return mst

#test
nodes = list("ABCDEFG")
edges = [ ("A", "B", 7), ("A", "D", 5),
          ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
	  ("C", "E", 5),
	  ("D", "E", 15), ("D", "F", 6),
	  ("E", "F", 8), ("E", "G", 9),
	  ("F", "G", 11)]

print "prim:", prim( nodes, edges )
#output
#prim: [('A', 'D', 5), ('D', 'F', 6), ('A', 'B', 7), ('B', 'E', 7), ('E', 'C', 5), ('E', 'G', 9)]

