"""
Given an integer numRows, return the first numRows of Pascal's triangle.
"""

# dynamic programming, O(num_rows^2)
def pascalTri(num_rows):
	triangle = []

	for row_num in range(num_rows):
		# The first and last row elements are alway 1 
		row = [None for _ in range(row_num + 1)]
		row[0], row[-1] = 1, 1 

		# Each triangle element is equal to the sum of the elements
		# above-and-to-the-lef and above-and-to-the-right 
		for j in range(1, len(row) -1):
			row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

		triangle.append(row) 
	return triangle 
