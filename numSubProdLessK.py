"""
Example 3: 713. Subarray Product Less Than K.

Given an array of positive integers nums and an integer k, 

# Windows: return the number of subarrays (no need to find the max, return all) 

# Constraint: where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
"""

def numSubProdLessK(nums, k):

	# edge case 
	if k <= 1:
		return 0 

	# initialize the answer and left pointer 
	ans = left = 0

	# keep track of current product, all positive, at least 1 
	curr = 1 

	# check all windows 
	for right in range(len(nums)):

		# expand by including rightmost 
		curr *= nums[right]

		# check constraint, fix broken window 
		while curr >= k: 

			curr //= nums[left]
			left += 1 

		# no need to find max, return all lengths of valid windows
		ans += right - left + 1 

	return ans 




















