"""
Example 1: 199. Binary Tree Right Side View

Given the root of a binary tree, 

imagine yourself standing on the right side of it. 

Return the values of the nodes you can see ordered from top to bottom.
"""
# find the rightmost node of each level 

# O(n)
class Solution:

	def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

		if not root:
			return []


		ans = []

		queue = deque([root])


		while queue:

			# entire level in our queue 
			current_length = len(queue)


			# the last element of the queue 
			# will have the rightmost node of the current level

			ans.append(queue[-1].val)  # this is the rightmost node for the current level

			for _ in range(current_length):

				node = queue.popleft()


					# add the left child before the right child 
					# the nodes are in order in our queue
					if node.left:
						queue.append(node.left)

					if node.right:
						queue.append(node.right) 


		return ans 

