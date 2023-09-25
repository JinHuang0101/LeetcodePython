"""
Example 2: 2260. Minimum Consecutive Cards to Pick Up

Given an integer array cards, 

find the length of the shortest subarray 

that contains at least one duplicate. 

If the array has no duplicates, return -1.

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] 

which contain a matching pair of cards with value 3. 

Note that picking up the cards [4,2,3,4] is also optimal.

his question is equivalent to: 

what is the shortest distance between any two of the same element?

If we go through the array and use a hash map to record the indices for every element, 

we can iterate over those indices to find the shortest distance. 

The shortest subarray that contains a duplicate will have the first and last element be the duplicate 

Therefore, we just need to find the shortest distance between any two of the same element.
"""

from collections import defaultdict 

# O(n)
def minCardPickup(cards):

	dic = defaultdict(int)

	# cards = [1, 2, 6, 2, 1]
	# map 1: [0, 4], 2: [1, 3] 6: [2]
	# Iterate over the array once and record the position of each element in a hash map. 
	#  The keys to the hash map will be the element, and the value will be an array of all the indices it appears at.
	for i in range(len(cards)):
		dic[cards[i]].append(i)

	ans = float('inf')


	# Because we iterate on the indices in ascending order, 
	# each array within the hash map will also be sorted ascending.
	# Now we can check each element individually. 
	# To find the minimum distance, we just need to check all adjacent pairs 
	#because the array is sorted.


	for key in dic:
		arr = dic[key]

		for i in range(len(arr)-1):
			ans = min(ans, arr[i+1] - arr[i] + 1)

	return ans if ans < float('inf') else -1 