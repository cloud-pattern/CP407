#Dijkstra's Algorithm
#Robert Florance | 11.17.11 | CP407
import sys

GRAPH = [[0,1,1],[0,3,4],[1,2,1],[2,3,3],[2,4,7],[3,4,2]] #EDGE = [FROM, TO, DIST]
NODES = [0, 1, 2, 3, 4]
live_nodes = []
dead_nodes = []
distances = []
prev_nodes = []

if len(sys.argv) > 1:	start = sys.argv[1]
else: start = 0 
if len(sys.argv) > 2:	end = sys.argv[2]
else: end = 4

#initialize d to high values
for node in NODES:
	distances.insert(node, 111)
	prev_nodes.insert(node, -1)

#add our start node to the list of live nodes
live_nodes.append(start)
distances[start] = 0

def extract_min():
	global distances, prev_nodes, live_nodes, dead_nodes

	smallest_dist = 1111
	smallest_node = -1
	for node in live_nodes:
		if distances[node] < smallest_dist:
			smallest_node = node
			smallest_dist = distances[node]
	live_nodes.remove(smallest_node)
	print "extracted smallest node: ", smallest_node
	return smallest_node 

def relax_neighbors(node):
	global distances, prev_nodes, live_nodes, dead_nodes
	
	for edge in GRAPH:
		if edge[0] == node: #If the FROM index of the inner list is, in fact, the node we are talking about
			if edge[1] not in dead_nodes: #If the TO index of the inner list is not an already settled node
				if distances[edge[1]] > distances[edge[0]] + edge[2]: #If we have a beter route to that node via the given
					print 'found better route to node ', edge[1]
					distances[edge[1]] = distances[edge[0]] + edge[2] #update distance
					prev_nodes[edge[1]] = edge[0] #update previous node
					live_nodes.append(edge[1]) #make this node live	
while len(live_nodes) > 0:
	
	u = extract_min()
	dead_nodes.append(u)
	relax_neighbors(u)

def print_route(node):
	global prev_nodes
	print prev_nodes[node]
	if prev_nodes[prev_nodes[node]]: print_route(prev_nodes[node]) 


print_route(end)
print distances[end]
print live_nodes
