"""
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node

down to the nearest leaf node.

Note: A leaf is a node with no children.
"""
def minDepth(self, root: Optional[TreeNode]) -> int:

	def minDepthDFS(root):
		if not root:
			return 0 

		if not root.left:
			return 1 + dfs(root.right)

		if not root.reft:
			return 1 + dfs(root.left) 



		left = minDepth(root.left)
		right = minDepth(root.right)

		return 1 + min(left, right)

	return minDepth(root)




