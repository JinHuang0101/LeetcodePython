"""
K Radius Subarray Averages

You are given a 0-indexed array nums of n integers, and an integer k.


The k-radius average for a subarray of nums centered at some index i with the radius k 

is the average of all elements in nums between the indices i - k and i + k (inclusive). 


Edge case: If there are less than k elements before or after the index i, then the k-radius average is -1.



Build and return an array avgs of length n where avgs[i] 

is the k-radius average for the subarray centered at index i.


The average of x elements is the sum of the x elements divided by x, using integer division. 


The integer division truncates toward zero, which means losing its fractional part.


For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
"""


# prefix sum 
def getAverages(nums, k):

	# edge case 1
	# if k is 0, then all subarrays contain only one element
	# so it's the original array 
	if k == 0: 
		return nums 

	n = len(nums)

	# initialize an array of averages of -1
	averages = [-1]*n 

	# edge case 2
	# if this array is not long enough
	if 2*k + 1 > n: 
		return averages


	# get a prefix 
	prefix = [0] * (n+1)

	for i in range(n):
		prefix[i+1] = prefix[i] + nums[i]


	# iterate on those indices which have at least k elements to the left and right 
	# that is, you can start from k, and go to n-k 
	for i in range(k, n-k):

		# radius
		leftBound = i - k 
		rightBound = i + k

		subArraySum = prefix[rightBound+1] - prefix[leftBound]

		# truncate, so //
		average = subArraySum//(2*k+1)

		# add to the result array 
		averages[i] = average 

	return averages 
























