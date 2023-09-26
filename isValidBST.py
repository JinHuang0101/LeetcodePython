"""
Example 3: 98. Validate Binary Search Tree

Given the root of a binary tree, 

determine if it is a valid BST.
"""
class Solution:
	def isValidBST(self, root: Optional[TreeNode]) -> bool:

		# do a dfs
		def dfs(node, small, large):
			if not node:
				return True 

			if not(small < node.val < large):
				return False 

			# check the left, then node.val has to be the large
			left = dfs(node.left, small, node.val)

			# check the right, then node.val has to be the small
			right = dfs(node.right, node.val, large)

			# tree is a BST if left and right subtrees are both BSTs
			return left and right 

		return dfs(root, float("-inf"), float("inf"))

	