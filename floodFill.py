"""
flood fill 
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. 
You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, 
plus any pixels connected 4-directionally to the starting pixel of the same color 
as the starting pixel, plus any pixels connected 4-directionally to those pixels 
(also with the same color), and so on. 
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""

# DFS 
# paint the starting pixels, plus adjacent pixels of the same color, and so on
# Floodfill the starting pixel: change the color of that pixel to the new color
# Check the 4 neighboring pixels to make sure they are valid pixels of the same color
# and of the valid ones, floodfill those...
def floodFill(image, sr, sc, newColor):
	# image is a two dimensional array
	# row, collumn
	R, C = len(image), len(image[0])
	color = image[sr][sc]
	
	# if already new color, do nothing
	if color == newColor: return image  
	
	# DFS, all four directions
	def dfs(r, c):
		# condition: same neighbouring colors
		if image[r][c] == color:
			image[r][c] = newColor
			if r >= 1: dfs(r-1, c) # go up
			if r + 1 < R: dfs(r+1, c) # go down 
			if c >= 1: dfs(r, c-1) # go left 
			if c+1 < c: dfs(r, c+1) # go right 

	# Starting from the source pixel 
	dfs(sr, sc)
	return image  


