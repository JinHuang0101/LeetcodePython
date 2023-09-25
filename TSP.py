"""
Author: Jin Huang

Implement Travelling Salesman Problem using the nearest-neighbor heuristic.
"""

def solve_tsp(G):
	totalNodes = len(G)
	path = [0]
	visited = set([0])

	while len(visited) < totalNodes:
		currentNode = path[-1]
		nearestNeighbor = None 
		minDistance = float('inf')

		for neighbor in range(totalNodes):
			if neighbor not in visited and G[currentNode][neighbor]>0 and G[currentNode][neighbor]<minDistance:
				nearestNeighbor = neighbor
				minDistance = G[currentNode][neighbor]

		path.append(nearestNeighbor)
		visited.add(nearestNeighbor)

	path.append(0)
	return path 
