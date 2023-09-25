"""
Shuffle the Array
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
"""
def shuffle(self, nums: List[int], n:int)->List[int]:
	res = []

	
	for i in range(n // 2):
		res.append(nums[i])
		res.append(nums[i+ n//2])

	return res 
