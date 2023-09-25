"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

"""
def longestCommonPrefix(strs):
	result = ""
	i = 0 

	while True:
		try:
			sets = set(string[i] for string in strs)
			if len(sets) == 1:
				result += sets.pop()
				i+=1 
			else: break
		except Exception as e: 
			break 
	return result 

# O(n*m) where n is the number of strings in the input list, m is the length of the shortest string
def longestCommonPrefix(strs):
	# Assume the prefix is the shortest string in the list 
	pre = strs[0]

	# Iterate over all the other strings in the list and compare them with the prefix 
	# If match found, continue to the next string 
	for i in strs:

		# If no match, reduce the length of the prefix by one char at a time 
		# until a match is found or empty
		while not i.startswith(pre):
			pre = pre[:-1]
	
	# If all strings match the prefix, return the prefix 
	return pre 

