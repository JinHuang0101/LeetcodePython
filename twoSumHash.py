"""
Example 1: 1. Two Sum

Given an array of integers nums and an integer target, 

return indices of two numbers 

such that they add up to target. 

You cannot use the same index twice.
"""

# hashing O(n)
def twoSumHash(nums, target):

	# build a hash map as iterating along the array
	# map each value to its index 

	dic = {}

	# get a numm first 
	# get the complement of that num at the same time

	for i in range(len(nums)):
		num = nums[i]

		complement = target - num 

		# num is in the array for sure 
		# if complement is also in the array,
		# then pair found
		if complement in dic: 
			return [i, dic[complement]]

		# if complement not in dic
		# push the current num and its index into the dict
		dic[num] = i  

	return [-1, -1]