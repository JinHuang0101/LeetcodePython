"""
You are given an integer array nums consisting of n elements, and an integer k.

Constraints: Find a 1 contiguous subarray 2 whose length is equal to k 

Result: track the max value: that has the maximum average value and return this value. 

Any answer with a calculation error less than 10-5 will be accepted.
"""


# sliding window 
# find the max sum, divide at the end

def findMaxAv(nums, k):

	# get the first sum 
	sum = 0 

	# find the average of the first k elements 
	for i in range(k):
		sum += nums[i] 

	# initialize result to this first sum 
	result = sum 

	# find the other windows 
	for right in range(k, len(nums)):

		# inclulde right, drop left
		sum += nums[right] - nums[right - k]

		# keep the max 
		result = max(result, sum)

	# get the max average 
	return result / k 



