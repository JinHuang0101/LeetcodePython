"""
Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

# fast and slow pointer, O(n) 
def middleNode(head):

	slow = fast = head 

	while fast and fast.next:
		slow = slow.next 
		fast = fast.next.next 

	return slow 