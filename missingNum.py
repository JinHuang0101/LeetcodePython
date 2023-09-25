"""
Missing Number

Given an array nums containing n distinct numbers in the range [0, n], 

return the only number in the range that is missing from the array.

# the length of the array is n 

Input: nums = [3,0,1]
Output: 2

Input: nums = [0,1]
Output: 2

"""

# hash: O(n)
def missingNum(nums):

	# insert each elment of nums into a set 
	# so that we have O(1) when query the num_set
	num_set = set(nums)


	# get the complete array 

	# only one is missing
	n = len(nums) + 1

	# see if any number from the complete array not in num_set
	for number in range(n):
		if number not in num_set:
			return number



