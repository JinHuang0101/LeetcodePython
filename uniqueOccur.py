"""
Unique Number of Occurrences

Given an array of integers arr, 

return true if the number of occurrences of each value in the array is unique 

or false otherwise.

It's the number of occurences of each value.

Not distinct values in an array 

"""
def uniqueOccur(arr):
	dic = {}

	# create a hash map 
	# keep track of the number of occurences of each value
	for i in arr: 
		if i in dic: 
			dic[i] += 1 

		else:
			dic[i] = 1 

	# If all occurences are unique, then the len(unique (dic.values)) 
	# should be the same as the len(unique arr values) 
	if len(set(dic.values())) != len(set(arr)):
		return False 

	return True 


