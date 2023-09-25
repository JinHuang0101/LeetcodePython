"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
"""

# Two pointers
# Only need to return the index, no need to remove the duplicates
# Find the index that divides unique and the remaining deleted elements 

def removeDuplicates(nums):
	size = len(nums)
	insertIndex = 1 
	for i in range(1, size):

		# If found unique element 
		if nums[i-1] != nums[i]:

			# Update insertIndex in the main array
			nums[insertIndex] = nums[i]

			# Increment insertIndex count by 1 
			insertIndex += 1 
	return insertIndex 




