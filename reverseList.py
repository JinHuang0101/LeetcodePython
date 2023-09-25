
# O(n)
def reverse_list(head):

	prev = None 
	curr = head 

	while curr:
		
		# first, don't lose the next node
		next_node = curr.next 

		# reverse the direction of the pointer
		curr.next = prev 

		# set the current node to prev for the next node
		prev = curr 	

		# move on 
		curr = next_node

	return prev 

