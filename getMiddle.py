"""
Example 1: Given the head of a linked list 

with an odd number of nodes head, 

return the value of the node in the middle.

For example, 

given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.

# the difficulty in this problem comes from the fact that we don't know how long the linked list is.

"""

# Option 1: iterate through the linked list once with a dummy pointer to find the length, 
# then iterate from the head again once we know the length to find the middle.
def get_middle(head):

	length = 0 

	dummy = head 

	while dummy:
		length += 1 

		dummy = dummy.next  

	for _ in range(length//2):
		head = head.next 

	return head.val 


# fast and slow pointers 
"""
If we have one pointer moving twice as fast as the other, 

then by the time it reaches the end, 

the slow pointer will be halfway through since it is moving at half the speed.
"""

# O(n)
def get_middle(head):
	slow = head 
	fast = head 

	while fast and fast.next:
		slow = slow.next 
		fast = fast.next.next 

	return slow.val 


