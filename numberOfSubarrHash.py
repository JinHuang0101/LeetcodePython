"""
Example 5: 1248. Count Number of Nice Subarrays

Given an array of positive integers nums and an integer k. 

Find the number of subarrays with exactly k odd numbers in them.

For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. 

The subarrays with 3 odd numbers in them are [1, 1, 2, 1, 1] and [1, 1, 2, 1, 1].

Constraint: odd number count 
"""

from collections import defaultdict

def numberOfSubarrays(nums, k):

	counts = defaultdict(int)

	counts[0] = 1 

	ans = curr = 0 

	# at each element 
	for num in nums:

		# use curr to track the number of odd numbers 
		# use mod 2, if odd, then x % 2 = 1 
		curr += nums % 2 

		# at each element, query curr - k 
		ans += counts[curr - k]

		counts[curr] += 1 

	return ans 


