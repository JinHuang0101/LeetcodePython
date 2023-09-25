"""
Author: Jin Huang
Apply BFS to solve a 2-D puzzle of size M*N.
"""

from collections import deque


def buildPath(parent, destination):
	path = []
	current = destination
	while current is not None:
		path.append(current)
		current = parent[current]
	return path[::-1]



def validNeighbors(puzzle, position):
	neighbors=[]
	directions = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}

	for direction in directions.values():
		newRow = position[0] + direction[0]
		newCol = position[1] + direction[1]
		if 0<=newRow<len(puzzle) and 0<=newCol<len(puzzle[0]) and puzzle[newRow][newCol]=="-":
			neighbors.append((newRow,newCol))
	return neighbors


def solve_puzzle(board, source, destination):
	queue = deque()
	visited = set()
	parent = {}

	queue.append(source)
	visited.add(source)
	parent[source]=None 

	while len(queue)>0:
		currentCell = queue.popleft()
		if currentCell == destination:
			break 
		neighbors = validNeighbors(board, currentCell)

		for neighbor in neighbors:
			if neighbor not in visited:
				queue.append(neighbor)
				visited.add(neighbor)
				parent[neighbor]=currentCell 

	if destination not in visited:
		return None 

	path = buildPath(parent, destination)

	directions = ""
	for i in range(1, len(path)):
		row = path[i][0] - path[i-1][0]
		col = path[i][1] - path[i-1][1]
		if row == 0 and col == -1:
			directions += "L"
		elif row == 0 and col == 1:
			directions += "R"
		elif row == -1 and col == 0:
			directions += "U"
		elif row == 1 and col == 0:
			directions += "D"

	return path, directions  

