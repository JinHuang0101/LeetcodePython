"""
Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

# recursion 
# O(n + m)
def mergeTwoLinked(self, l1, l2):
	
	# edge cases
	if l1 is None:
		return l2

	elif l2 is None:
		return l1 

	elif l1.val < l2.val:
		l1.next = self.mergeTwoLinked(l1.next, l2)
		return l1 
	else:
		l2.next = self.mergeTwoLinked(l1, l2.next)
		return l2 


