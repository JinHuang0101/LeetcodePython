"""
Duplicate zeros 
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
"""
# O(N)
def duplicateZeros(arr):
	# don't return anything, modify arr in-place 
	possible_dups = 0 
	length = len(arr) - 1 

	# find the number of zeros to be duplicated 
	for left in range(length + 1):

		# stop when left points behond the last element in the original list 
		# which would be part of the modified list 
		# out of boundary 
		if left > length - possible_dups:
			break 

		# count the zeros 
		if arar[left] == 0:
			# edge case: this zero cannot be duplciated, no space 
			# as left is pointing to the last element which could be included 
			if left == length - possible_dups:
				arr[length] = 0 # for this zero we just copy it without duplication 
				length -= 1 
				break 
			possible_dups += 1 
	# start backwards from the last element which would be part of new list 
	last = length - possible_dups 

	# copy zero twice, and non zero once 
	for i in range(last, -1, -1):
		if arr[i] == 0:
			arr[i + possible_dups] = 0 
			possible_dups -= 1 
			arr[i + possible_dups] = 0 
		else:
			arr[i + possible_dups] = arr[i]

