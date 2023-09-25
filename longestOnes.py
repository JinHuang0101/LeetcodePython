"""
Given a binary array nums and an integer k, 

return the maximum number of consecutive 1's in the array 

if you can flip at most k 0's.

"""


# sliding window 
def longestOnes(nums, k):

	left = 0 

	for right in range(len(nums)):

		# if include a 0 
		k -= 1 - nums[right]

		if k < 0:
			k += 1 - nums[left]
			left += 1 

	return right - left + 1 
	 