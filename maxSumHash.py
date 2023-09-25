"""
Example 3: 2342. Max Sum of a Pair With Equal Sum of Digits

Given an array of integers nums, 

find the maximum value of nums[i] + nums[j], 

where nums[i] and nums[j] have the same digit sum

(the sum of their individual digits). 

Return -1 if there is no pair of numbers with the same digit sum.

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

similar to grouping anagrams 

In the first example, groups were identified by their sorted string. 

In this problem, we can identify a group by its digit sum. 

We iterate through the array 

and group all the numbers with the same digit sum together in a hash map. 

iterate over that hash map and for each group with at least 2 elements, find the 2 max elements by sorting.
"""
from collections import defaultdict 

# O(nlogn)
def maxSum(nums):

	def get_digit_sum(num):
		digit_sum = 0 

		while num:
			digit_sum += num % 10 
			num //= 10 

		return digit_sum 


	dic = defaultdict(list)

	for num in nums:
		digit_sum = get_digit_sum(num)
		dic[digit_sum].append(num)


	ans = -1 

	for key in dic:
		curr = dic[key]

		if len(curr) > 1:
			curr.sort(reverse=True)
			ans = max(ans, curr[0] + curr[1])

	return ans 



# Optimization: only save the max number seen so far for each digit sum
# O(n)

from collections import defaultdict 

def maxSum(nums):

	def get_digit_sum(num):
		digit_sum = 0 

		while num:
			digit_sum += num % 10 
			num //= 10 

		return digit_sum 

	dic = defaultdict(int)

	ans = -1 

	for num in nums:
		digit_sum = get_digit_sum(num)

		if digit_sum in dic:
			ans = max(ans, num + dic[digit_sum])

		dic[digit_sum] = max(dic[digit_sum], num)


	return ans 























