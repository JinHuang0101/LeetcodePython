"""
Example 2: Given a sorted array of unique integers and a target integer, 

return true if there exists a pair of numbers that sum to target, 

false otherwise. 

This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
"""

def checkTargetPair(nums, target):
	# initalize two pointers
	left = 0 
	right = len(nums) -1 

	# iterate the array 
	while left < right:

		# curr is the sum of the current two numbers 
		curr = nums[left] + nums[right] 

		# found 
		if curr == target:
			return True 

		# if not, because they are sorted, 
		if curr > target:  # decrease the right 
			right -= 1 

		if curr < target:   # increase the left 
			left += 1 
	return False 
	

