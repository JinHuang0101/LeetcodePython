"""
Example 1: Given an array of positive integers nums and an integer k, 

find the length of the longest subarray 

whose sum is less than or equal to k. 

"""

# sliding window 

def find_length(nums, k):

	# curr is the sum of the current window 
	left = curr = ans = 0 

	# move the right pointer 
	for right in range(len(nums)):
		curr += nums[right]

		# compare curr to target, as long as the window is not broken  
		while curr > k:

			# if exceeds, drop the leftmsot 
			curr -= nums[left]
			left += 1 

		ans = max(ans, right - left +1)   # only keep the max length of subarray 

	return ans 
