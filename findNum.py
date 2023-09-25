"""
Example 3: Given an integer array nums, 

find all the numbers x in nums 

that satisfy the following: 

x + 1 is not in nums, and x - 1 is not in nums.
"""

# conver the input array to a set
# O(n)
def find_numbers(nums):
	
	# result array
	ans = []

	# convert the input array to a set
	nums = set(nums)

	for num in nums:

		if (num + 1 not in nums) and (num - 1 not in nums):    # O(1)
			ans.append(num) 

	return ans 



