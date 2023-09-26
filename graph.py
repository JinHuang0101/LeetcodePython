from collections import defaultdict 

# input format 1: array of directed edges
def build_graph(edges):
	graph = defaultdict(list)

	for x, y in edges:
		graph[x].append(y)

		# if undirected graph
		# graph[y].append(x)
	return graph 

# input format 2: adjacency list 

# input format 3: adjacency matrix 
"""
If graph[i][j] == 1, that means there is an outgoing edge from node i to node j. 
"""






















