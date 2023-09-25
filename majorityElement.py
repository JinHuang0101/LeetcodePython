"""
Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 

You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3
"""
def majority(nums):
	
	# Initiate the target count: [n / 2] 
	majority_count = len(nums)//2 

	# Iterate through the array, check for duplicates  
	for num in nums: 
		count = sum(1 for elem in nums if elem == num)

		if count > majority_count:
			return num  






