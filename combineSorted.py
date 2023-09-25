"""
Example 3: Given two sorted integer arrays arr1 and arr2, 

return a new array that combines both of them 

and is also sorted.
"""

def combineSorted(arr1, arr2):

	# initialize the answer array 
	ans = []

	# initialize two pinters 
	i = j = 0 

	# iterate two arrays at the same time 
	while i < len[arr1] and j < len[arr2]:

		# compare 
		if arr1[i] < arr2[j]:
			ans.append(arr1[i])
			i += 1 

		else:
			ans.append(arr2[j])
			j += 1 

	# leftover, append the rest of it 
	while i < len(arr1):
		ans.append(arr1[i])
		i += 1 

	while j < len(arr2):
		ans.append(arr2[j])
		j += 1 

	return ans 
	