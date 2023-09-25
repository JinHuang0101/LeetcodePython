"""
Example 4: Given an integer array nums and an integer k, 

find the sum of the subarray with the largest sum whose length is k.

Constraints:
1. length is k -> window size 
2. subarray with the largest sum -> pick max 
"""


def best_sub(nums, k):

	# keep track of sum 
	curr = 0 

	# find the first k sum
	for i in range(k):
		curr += nums[i]


	# initialize the first k sum as ans 
	ans = curr 

	# window right end, right to k 
	for i in range(k, len(nums)):

		# include right, then drop left 
		curr += nums[i] - nums[i - k] 

		# constraint fulfilled, keep track of the max
		ans = max(ans, curr)

	return ans 
	


