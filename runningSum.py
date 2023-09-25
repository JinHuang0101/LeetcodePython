"""
Given an array nums. 

We define a running sum of an array as 

runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

"""

# We can rewrite the nums array in-place
# use input array for output

def runningSum(nums):

	# Like a dynamic array
	# Result [i] = sum (result[i-1]+ nums[i])
	# Build up the array from left to right
	for i in range(len(nums)):
		nums[i] += nums[i-1]

	return nums 



