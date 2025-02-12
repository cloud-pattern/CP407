#Generate connected graphs
import random, sys

def complete_graph(number_of_nodes):
	graph = []
	for i in range(number_of_nodes):
		from_node = i
		for j in range(number_of_nodes):
			if j != i:
				to_node = j
				edge_value = random.randint(1,10)
				graph.append([from_node, to_node, edge_value])
	return graph

def complete_graph_tuples(number_of_nodes):
	graph = []
	for i in range(number_of_nodes):
		from_node = str(i)
		for j in range(number_of_nodes):
			if j > i:
				to_node = str(j)
				edge_value = random.randint(1,10)
				graph.append((from_node, to_node, edge_value))
	return graph

def remove_edges(graph):
	length = len(graph)-1
	#print 'Removing edges: '
	for i in range(length):
		if i < len(graph):
			delete = random.randint(1,10)
			if delete < 6: #***CHANGE THIS NUMBER***
				p = graph.pop(i)
				#print p

def one_edge_each(graph, number_of_nodes):

	for i in range(number_of_nodes):
		
		from_node = i
		to_node = random.randint(0, number_of_nodes-1)
		
		#make sure we dont make an edge going to itself
		while to_node == i:
			to_node = random.randint(0, number_of_nodes-1)
		
		edge_value = random.randint(1, 10)
		
		graph.append([from_node, to_node, edge_value])

def sure_route(graph, number_of_nodes):
	#create a route that sequentially reaches the last node
	for i in range(number_of_nodes-1):
		from_node = i
		to_node = i+1
		edge_value = 1
		
		graph.append([from_node, to_node, edge_value])

def cheater_route(graph, number_of_nodes):
	#append an edge that goes from start to end with distance of 1
	graph.append([0,number_of_nodes-1,1])


#number_of_nodes = 5
#graph = []
#graph = complete_graph_tuples(number_of_nodes)
#remove_edges(graph)
#print graph

