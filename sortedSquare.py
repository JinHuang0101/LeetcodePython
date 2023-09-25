"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Trick:
positive and negative numbers 

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""

# Two pointers, compare the squares 
def sortedSquare(nums):
	n = len(nums)

	# result arr 
	squares = [0 for x in range(n)]

	# largest value at the right end
	highestSquareIndx = n - 1 

	# Two pointers, start from the ends 
	left, right = 0, n-1

	# iterate 
	while left <= right:
		leftSquare = nums[left] * nums[left]
		rightSquare = nums[right] * nums[right]

		# compare 
		if leftSquare > rightSquare:
			squares[highestSquareIndx] = leftSquare 
			left += 1 

		else:
			squares[highestSquareIndx] = rightSquare 
			right -= 1 

		# move highestSquareIndx towards left 
		highestSquareIndx -= 1 

	return squares 
	




