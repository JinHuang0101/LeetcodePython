"""
Example 4: 560. Subarray Sum Equals K

Given an integer array nums and an integer k, 

find the number of subarrays whose sum is equal to k.
"""

# prefix sum and hash 
#Because the array can have negative numbers, 
# the same prefix can occur multiple times. 
# We use a hash map counts to track how many times a prefix has occurred.

from collections import defaultdict 

# O(n)
def subarraySum(nums):

	counts = defaultdict(int)

	# empty prefix 
	counts[0] = 1 

	ans = curr = 0 

	for num in nums:

		# curr is the prefix sum for this input 
		curr += num  

		# if curr-k has been seen prior 
		# At every index i, the frequency of curr - k is equal to the number of subarrays 
		# whose sum is equal to k that end at i. 
		# Add it to the answer.
		ans += counts[curr - k]


		counts[curr] += 1  

	return ans 

