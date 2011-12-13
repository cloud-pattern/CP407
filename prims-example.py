#Prim's Algorithm
#Robert Florance | 12.2.11 | CP407
import sys, genGraph
from collections import defaultdict
from heapq import *

#TEST GRAPHS
NODES_A = list("ABCDEFG")
GRAPH_A =  [ ("A", "B", 7), ("A", "D", 5),
          ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
	  ("C", "E", 5),
	  ("D", "E", 15), ("D", "F", 6),
	  ("E", "F", 8), ("E", "G", 9),
	  ("F", "G", 11)]

counter = 0

def prims(nodes, graph):

	connections = defaultdict(list)
	#'complete' the graph, by making every connection 2-way
	for node_1, node_2, value in graph:
		connections[node_1].append((value, node_1, node_2))
		connections[node_2].append((value, node_2, node_1))
	print 'Graph:', connections
	minimum_spanning_tree = []
	#Add the first node to the used_nodes set
	used_nodes = set(nodes[0])
	#Add edges that are connected to the first node to the usable_edges list
	usable_edges = connections[nodes[0]][:]
	#Order the usable edges to keep the smallest on top
	heapify(usable_edges)

	while usable_edges:
		#Of the connected edges, get the smallest:	
		value, node_1, node_2 = heappop(usable_edges)
		counter +=1
		if node_2 not in used_nodes:
			
			used_nodes.add(node_2)
			minimum_spanning_tree.append((node_1, node_2, value))

			for edge in connections[node_2]:
				counter +=1
				if edge[2] not in used_nodes:
					#Add the edges we are now connected to
					heappush(usable_edges, edge)
	return minimum_spanning_tree


result = prims(NODES_A, GRAPH_A)

print 'minimum spanning tree: ', result
print 'steps: ', counter

#output
#[('A', 'D', 5), ('D', 'F', 6), ('A', 'B', 7), ('B', 'E', 7), ('E', 'C', 5), ('E', 'G', 9)]
