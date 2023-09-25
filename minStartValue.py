"""
Given an array of integers nums, you start with an initial positive value startValue.


In each iteration, you calculate the step by step sum of startValue

 plus elements in nums (from left to right).


Return the minimum positive value of startValue 

If sum less than 1, invalid: such that the step by step sum is never less than 1.

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
"""
# startValue can be any positive value
# Constraint: sum cannot be less than 1
# Key: the min startValue is the value that makes 
# the min element in the step-by-step sums equal to exactly 1
# startValue = 0, minVal + startValue = 1 


# prefix sum 

def minStartValue(nums):

	# set a min_val 
	min_val = 0 

	# total for current step-by-step total 
	total = 0 

	# iterate over the array and get the min step-by-step total
	for num in nums:
		total += num 
		min_val = min(min_val, total)    # keep track of the min positive value of startValue


	# change the min step-by-step total to 1 
	# by increasing the startValue from 0 to -min_val + 1 
	# which is the min startValue we want 
	return -min_val + 1






