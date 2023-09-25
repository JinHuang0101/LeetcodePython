"""
Example 4: 392. Is Subsequence.

Given two strings s and t, 

return true if s is a subsequence of t, 

or false otherwise.

A subsequence of a string is a sequence of characters 

that can be obtained by deleting some (or none) of the characters 

from the original string, while maintaining the relative order of the remaining characters. 

For example, "ace" is a subsequence of "abcde" while "aec" is not.
"""


# check if s is in i, O(m + n) 
def isSub(s, t):

	# two pointers 
	i = j = 0 

	# loop 
	while i < len(s) and j < len(t):
		# check if s in t 
		if s[i] == t[j]:

			# increment i, check the next s char
			i += 1

		# if not anchor i, increment j 
		j += 1 

	# if i pointer can iterate through the entire s string, then True 
	return i == len(s)   



