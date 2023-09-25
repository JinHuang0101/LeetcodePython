"""
Example 1: 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 

determine if the input string is valid. 

The string is valid if all open brackets are closed by the same type of closing bracket in the correct order, 

and each closing bracket closes exactly one open bracket.

For example, s = "({})" and s = "(){}[]" are valid, but s = "(]" and s = "({)}" are not valid.

# Stacks are useful for string matching because it saves a "history" of the previous characters. 
"""

# O(n) 
def isValid(s):

	stack = []


	# how to associate the openning and closing brackets together?
	# use a hash map to map each opening bracket to its closing bracket 
	matching = {"(":")", "[":"]", "{":"}"}

	for c in s: 

		# if c is an opening bracket
		if c in matching:
			stack.append(c)
		
		# if c is a closing bracket
		# then should match the last element on the stack
		else:

			# if stack is empty
			# no previous opening parenthesis
			if not stack:
				return False 

			previous_opening = stack.pop()

			if matching[previous_opening] != c:
				return False 

	# should be empty stack in the end
	return not stack 



