"""
Example 2: 2270. Number of Ways to Split Array

Given an integer array nums, find the number of ways to split the array into two parts 

so that the first section has a sum greater than or equal to the sum of the second section. 

The second section should have at least one number.
"""

def waysToSplitArray(nums):

	n = len(nums)

	prefix = [nums[0]]

	# get the prefixes of all elements 
	for i in range(1, n):
		prefix.append(nums[i] + prefix[-1])


	# ans 
	ans = 0 

	# the second section has at least one number, so range(n-1)
	for i in range(n-1):
		# to the left of i
		left_section = prefix[i] 

		# to the right of i
		# prefix[-1] because this is the initial prefix of the entire prefix array
		right_section = prefix[-1] - prefix[i] 

		# compare 
		if left_section >= right_section:
			ans += 1 

	return ans 


# Option 2 
# No prefix array, get the total sum first 

def waysToSplitArray(nums):

	ans = left_section = 0 

	total = sum(nums)

	for i in range(len(nums) - 1):

		left_section += nums[i] 

		right_section = total - left_section 

		if left_section >= right_section:
			ans += 1 

	return ans 

























