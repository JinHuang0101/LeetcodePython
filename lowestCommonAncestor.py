"""
Bonus example: 236. Lowest Common Ancestor of a Binary Tree

Given the root of a binary tree and two nodes p and q that are in the tree, 

return the lowest common ancestor (LCA) of the two nodes. 

The LCA is the lowest node in the tree that has both p and q as descendants 

(note: a node is a descendant of itself).
"""

class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		if not root:
			return None 

		if root == p or root == q:
			return root


		left = self.lowestCommonAncestor(root.left, p, q)
		right = self.lowestCommonAncestor(root.right, p, q)

		if left and right:
			return root 

		if left:
			return left 

		return right 