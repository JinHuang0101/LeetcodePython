"""
Palindrome linked list 
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Linked list: first get the list; then compare it to the reversed list
"""

# O(n)
def isPalindrome(self, head: ListNode) -> bool:
	vals = []
	current_node = head 

	# Copy the linked list into an array 
	while current_node is not None:
		vals.append(current_node.val)
		current_node = current_node.next 
	
	# check if it's a palindrome, 
	# make a reversed copy of the list
	# compare two lists
	return vals == vals[::-1]


# Two pointers 
def isPalindrome(s):
	# Initialize two pointers
	left = 0 
	right = len(s)-1 

	while left < right: 
		if s[left] != s[right]:
			return False 

		# move towards the middle 
		left += 1 
		right -= 1 

	return True 



