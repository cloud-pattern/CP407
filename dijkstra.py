#Dijkstra's Algorithm
#Robert Florance | 11.17.11 | CP407
import sys, genGraph

graphs = {
		'GRAPH_1':[[0,1,1],[0,3,7],[1,2,1],[2,3,3],[2,4,7],[3,4,2]], #01234
		'GRAPH_2':[[0,1,7],[0,3,1],[1,2,1],[2,3,3],[2,4,7],[3,4,2]], #034
		'GRAPH_3':[[0,1,7],[0,2,9],[0,5,14],[1,2,1],[1,3,5],[2,3,1],[2,5,4],[3,4,1],[4,5,1]], #012345
		'GRAPH_4':[[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [0, 2, 3], [1, 2, 9], [2, 3, 3], [3, 2, 9], [4, 1, 2]], #01234
		'GRAPH-GEN' : genGraph.complete_graph(5)
	}

GRAPH = []
NODES = []
live_nodes = []
dead_nodes = []
distances = []
prev_nodes = []

counter = 0

GRAPH = graphs[sys.argv[1]]
print 'GRAPH: ', GRAPH

#using the graph list of lists, make a list of nodes in the graph
for edge in GRAPH:
	if edge[0] not in NODES:
		NODES.append(edge[0])
	if edge[1] not in NODES:
		NODES.append(edge[1])

print 'NODES: ', NODES
	
#initialize d to high values
for node in NODES:
	distances.insert(node, 111)
	prev_nodes.insert(node, -1)

#add our start node to the list of live nodes
live_nodes.append(0)
distances[0] = 0
prev_nodes[0] = 0

def extract_min():
	global distances, prev_nodes, live_nodes, dead_nodes, counter

	smallest_dist = 1111
	smallest_node = -1
	for node in live_nodes:
		counter+=1
		if distances[node] < smallest_dist:
			smallest_node = node
			smallest_dist = distances[node]
	live_nodes.remove(smallest_node)
	return smallest_node 

def relax_neighbors(node):
	global distances, prev_nodes, live_nodes, dead_nodes, counter
	
	for edge in GRAPH:
		if edge[0] == node: #If the FROM index of the inner list is, in fact, the node we are talking about
			if edge[1] not in dead_nodes: #If the TO index of the inner list is not an already settled node
				counter +=1
				if distances[edge[1]] > distances[edge[0]] + edge[2]: #If we have a beter route to that node via the given
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

end = len(NODES) -1

print 'Best Route: '
print end
print_route(end)
print 'With a distance of: ', distances[end]

print counter, "steps taken"
