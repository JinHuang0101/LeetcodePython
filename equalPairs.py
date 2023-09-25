"""
Example 4: 2352. Equal Row and Column Pairs

Given an n x n matrix grid, 

return the number of pairs (R, C) 

where R is a row and C is a column, 

and R and C are equal if we consider them as 1D arrays.

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
"""


# O(n^2)
from collections import defaultdict 

def equalPairs(grid):

	def convert_to_key(arr):
		return tuple(arr)

	dic = defaultdict(int)

	for row in grid:
		dic[convert_to_key(row)] += 1 

	dic2 = defaultdict(int)

	for col in range(len(grid[0])):
		current_col = []

		for row in range(len(grid)):
			current_col.append(grid[row][col])

		dic2[convert_to_key(current_col)] += 1 

	ans = 0 

	"""
	If there are x rows that are identical to y columns, 
	then for each of the x rows, 
	it could match with any of the y columns. 
	This means there are x * y pairs.
	"""

	for arr in dic:
		ans += dic[arr] * dic2[arr]

	return ans 

