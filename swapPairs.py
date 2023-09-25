"""
Example: 24. Swap Nodes in Pairs

Given the head of a linked list, swap every pair of nodes. 

For example, given a linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6, return a linked list 2 -> 1 -> 4 -> 3 -> 6 -> 5.
"""

def swapPairs(head):

	# edge case: linked list has 0 or 1 node
	if not head or not head.next:
		return head 

	dummy = head.next 

	prev = None 

	while head and head.next:
		if prev:
			prev.next = head.next 
		prev = head 

		next_node = head.next.next 
		head.next.next = head 

		head.next = next_node 
		head = next_node 

	return dummy 