"""
Example 3: 1448. Count Good Nodes in Binary Tree

Given the root of a binary tree, 

find the number of nodes that are good. 

A node is good if the path between the root and the node 

has no nodes with a greater value.
"""

# O(n)
class solution:

	def goodNodes(self, root: TreeNode) -> int:

		def dfs(node, max_so_far):

			# base: if no node
			if not node:
				return 0

			# get the number of good nodes from the left subtree
			left = dfs(node.left, max(max_so_far, node.val))

			# get the number of good nodes from the right subtree 
			right = dfs(node.right, max(max_so_far, node.val))

			# then sum the left good nodes and right good nodes
			ans = left + right 

			# what do we do?
			if node.val >= max_so_far:
				ans += 1 

			return ans 

		return dfs(root, float("-inf"))




