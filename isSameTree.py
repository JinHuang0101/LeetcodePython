"""
Example 4: 100. Same Tree

Given the roots of two binary trees p and q, 

check if they are the same tree. 

Two binary trees are the same tree if they are structurally identical 

and the nodes have the same values.
"""

"""
recursive nature of binary trees
p.val = q.val
p.left and q.left are the same tree
p.right and q.right are the same tree

"""

# O(n)
class Solution:
	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

		if p == None and q == None:
			return True 

		if p == None or q == None:
			return False 

		if p.val != q.val:
			return False 



		left = self.isSameTree(p.left, q.right)
		right = self.isSameTree(p.right, q.right)

		return left and right 



























