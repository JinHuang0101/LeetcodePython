"""
Example 3: 844. Backspace String Compare

Given two strings s and t, return true if they are equal 

when both are typed into empty text editors. 

'#' means a backspace character.

For example, given s = "ab#c" and t = "ad#c", return true. 

Because of the backspace, the strings are both equal to "ac".
"""
# when we backspace, pop
# edge case where we backspace on an empty string 

def backspaceCompare(s, t):

	def build(s):
		stack = []

		for c in s: 
			
			if c != "#":
				stack.append(c) 

			elif stack:
				stack.pop()

		return "".join(stack)

	return build(s) == build(t)



