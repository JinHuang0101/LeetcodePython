"""
Longest Substring Without Repeating Characters

Given a string s, 

find the length of the longest substring 

without repeating characters.
"""

# sliding window 
from collections import defaultdic

def lengthOfLongestSubstring(s):

	chars = Counter()

	left = right = 0 

	res = 0 

	while right < len(s):
		r = s[right]
		chars[r] += 1 

		while chars[r] > 1:
			l = s[left]
			chars[l] -= 1 
			left += 1 

		res = max(res, right - left + 1)

		right += 1 
	return res 
	







# Sliding Window Optimized
# Instead of using a set to tell if a character exists or not, 
# we could define a mapping of the characters to its index. 
# Then we can skip the characters immediately when we found a repeated character.

# O(n)
def lengthOfLongestSubstring(s):

	n = len(s)

	ans = 0 

	# mp stores the current index of a char 
	mp = {}

	i = 0 

	# try to extend the range[i, j]
	for j in range(n):

		if s[j] in mp:
			i = max(mp[s[j]], i)

		ans = max(ans, j - i + 1)
		mp[s[j]] = j+1 

	return ans 

