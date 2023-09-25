"""
Counting Elements

Given an integer array arr, 

count how many elements x there are, 

such that x + 1 is also in arr. 

If there are duplicates in arr, count them separately.

Input: arr = [1,2,3]
Output: 2
"""
# hash_set removes duplicates 
# so loop over arr, not hash_set 
# check using HashSet 

def countElements(arr):
	

	hash_set = set(arr)

	count = 0 

	for x in arr:
		if x + 1 in hash_set:
			count += 1 

	return count 

