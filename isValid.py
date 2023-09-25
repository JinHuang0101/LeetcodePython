"""
Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "(]"
Output: false
"""

# O(n)
def isValid(str):

	# initiate a stack 
	stack = []

	# hash map to keep track of mappings. 
	# Makes adding more types of parenthesis easier 
	# hash map index is the closing bracket 
	mapping = {")":"(", "}": "{", "]":"[" }

	# for every bracket in the expression
	for char in str: 

		# if the char is a closing bracket
		if char in mapping:

			# pop the topmost element from the stack, if it is not empty 
			# otherwise assign a dummy value of "#" to the top_element variable 
			top_element = stack.pop() if stack else '#'

			if mapping[char] != top_element:
				return False 

		# if an open bracket, push it onto the stack
		else:
			stack.append(char)

	# In the end, if empty stack, then valid expression
	# If not, then invalid 
	return not stack 


