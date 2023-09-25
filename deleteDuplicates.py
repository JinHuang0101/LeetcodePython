"""
Remove Duplicates from Sorted List

Given the head of a sorted linked list, 

delete all duplicates such that each element appears only once. 

Return the linked list sorted as well.
"""

# O(n)
def deleteDuplicates (head):

	current = head 

	while current and current.next:
		if current.next.val == current.val:
			current.next = current.next.next 
		else:
			current = current.next 

	return head 

