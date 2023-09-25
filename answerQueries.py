"""
Example 1: Given an integer array nums, 

an array queries where queries[i] = [x, y] and an integer limit, 

return a boolean array that represents the answer to each query. 


A query is true if the sum of the subarray from x to y is less than limit, 

or false otherwise.

For example, 

given nums = [1, 6, 3, 2, 7, 2], 

queries = [[0, 3], [2, 5], [2, 4]], 

and limit = 13, 

the answer is [true, false, true]. 

For each query, the subarray sums are [12, 14, 12].
"""

# prefix 
# arry prefix where prefix[i] is the sum of all elements up to i 
# prefix find the sum of any subarray in O(1)
# sum of the subarray[i, j] = prefix[j] - prefix[i-1] (out of bounds i=0) or prefix[j] - prefix[i] + nums[i]

def answerQueries(nums, queries, limit):

	
	# createa a prefix array that includes the prefix at each index
	prefix = [nums[0]]

	# find the prefix at each index
	# save in the prefix array
	for i in range(1, len(nums)):
		prefix.append(nums[i] + prefix[-1])

	ans = []

	for x, y in queries: 
		
		curr = prefix[y] - prefix[x] + nums[x] 

		# return a Boolean answer
		ans.append(curr < limit)

	return ans 
	
























