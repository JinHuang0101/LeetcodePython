"""
Example 2: 2351. First Letter to Appear Twice

Given a string s, return the first character to appear twice. 

It is guaranteed that the input will have a duplicate character.
"""

# hash: O(n)
def repeatedChar(s):

	seen = set()

	# itearte the string 
	for c in s: 

		if c in seen:
			return c 

		see.add(c)

	return " "