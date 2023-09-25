"""
Reverse Linked List II

Given the head of a singly linked list and two integers left and right 

where left <= right, 

reverse the nodes of the list from position left to position right, 

and return the reversed list.
"""
def reverseBetween(head, m, n):
	"""
	: type head: ListNode 
	: type m: int 
	: type n: int 
	: rtype: ListNode
	"""

	if not head:
		return None 

	left, right = head, head 

	stop = False 

	def recurseAndReverse(right, m, n):
		nonlocal left, stop 

		# base case. Don't proceed
		if n == 1:
			return  

		# keep moving the right pointer one step forward until (n == 1)
		right = right.next  

		# keep moving left pointer to the right until we reach the proper node 
		# from where the reversal is to start 
		if m > l:
			left = left.next 

		# recurse with m and n reduced 
		recurseAndreverse(right, m-1, n-1)

		# in case both the pointers cross each other or become equal
		# we stop, dont swap data any further
		# we are done reversing at this point 
		if left == right or right.next == left: 
			stop = True 

		# until the boolean stop is false, swap data between the two pinters 
		if not stop:
			left.val, right.val = right.val, left.val 

			# move left one step to the right 
			# the right pointer moves one step back via backtracking 
			left = left.next 

	recurseAndreverse(right, m, n)
	return head 














