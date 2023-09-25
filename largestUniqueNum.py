"""
Largest Unique Number

Given an integer array nums, return the largest integer that only occurs once. 

If no integer occurs once, return -1.
"""

from collections import defaultdict

# hashmap, O(n) 
def largestUniqueNum(nums):

	counts = defaultdict(int)

	for num in nums:
		counts[num] += 1 

	result = -1 

	for key in counts.keys():

		if counts[key] == 1:
			result = max(result, key)
	
	return result 


