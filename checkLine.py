"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

Idea:
get 3 points, if straight line: 
the slopes of the lines from the 3rd point to the 2nd point
...and the 2nd point to the 1st point must be equal 
(y-y1)/(x-x1) = (y1-y0)/(x1-x0)

edge case: divded by zero 
change to multiplication: 
(x1-x0)(y-y1)=(x-x1)*(y1-y0)
"""
def checkStraightLine(coordinates):
	(x0, y0), (x1, y1) = coordinates[:2]
	for x, y in coordinates:
		if (x1-x0)*(y-y1) != (x-x1)*(y1-y0):
			return False 
	return True  


