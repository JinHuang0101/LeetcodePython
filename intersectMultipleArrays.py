"""
Example 2: 2248. Intersection of Multiple Arrays

Given a 2D array nums that contains n arrays of distinct integers, 

return a sorted array containing all the numbers that appear in all n arrays.


For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], 

return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
"""

# n arrays of distinct integers -> means a number appears n times if and only if it appears in all arrays

def intersection(nums):


	# use a hash map to count the frequency of elements 
	counts = defaultdict(int)

	# iterate over each of the inner arrays and update counts with every element 
	for arr in nums:
		for x in arr:
			counts[x] += 1 


	n = len(nums)

	ans = []

	# iterate over hash map to see which numbers appear n times 
	for key in counts: 
		if counts[key] == n:
			ans.append(key)

	return sorted(ans)


