"""
Example 2: 112. Path Sum

Given the root of a binary tree and an integer targetSum, 

return true if there exists a path from the root to a leaf 

such that the sum of the nodes on the path is equal to targetSum, 

and return false otherwise.
"""



def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


	# integer curr represents the current sum of the nodes from the root to the current node
	def dfs(node, curr):

		# base: empty tree
		if not node:
			return False 

		# base: leaf; if both children are null, then the node is a leaf 
		if node.left == None and node.right == None:
			return (curr + node.val) == targetSum 

		# if not leaf, continue down the left or the right 
		# have to add the current node's value to curr
		curr += node.val 

		left = dsf(node.left, curr)

		right = dfs(node.right, curr)

		return left or right 

	return dfs(root, 0) # start from the first node, there's no node before it, so sum is 0



