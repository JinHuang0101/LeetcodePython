"""
Check if Array Is Sorted and Rotated
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

[A[i] == B[(i+x) % A.length], where % is the modulo operation.
Input: nums = [3,4,5,1,2]
Output: true
"""
def checkSortedRotated(nums):
	# sort the list 
	numsSorted = sorted(nums)

	# iterate over all list elements 
	for i in range(len(nums)):
		# check every rotate option with the sorted list
		# if found return True 
		if nums[i:] + nums[:i] == numsSorted:
			return True 

	return False 
	

