"""
Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

# two pointers
# O(m + n)
def mergeAlternately(word1, word2):

	# get the lengths of two strings
	m = len(word1)
	n = len(word2)

	# initialize two pointers 
	i = 0
	j = 0 

	# initialize the result 
	result = []

	# iterate
	while i < m or j < n:
		if i < m:
			result += word1[i]
			i+=1 
		if j < n:
			result += word2[j]
			j += 1 

	# return the string
	return "".join(result)



