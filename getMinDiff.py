"""
Example 2: 530. Minimum Absolute Difference in BST

Given the root of a BST, 

return the minimum absolute difference 

between the values of any two different nodes in the tree.
"""

class Solution:
	def getMinDiff(self, root: Optional[TreeNode])-> int:

		# get all node values from min to max
		# i.e., sort the array
		# Then min absolute diff = difference between adjacent elements in the sorted array
		values = []

		# do a dfs 
		def dfs(node):

			if not node:
				return 

			left = dfs(node.left)
			values.append(node.val)
			right = dfs(node.right)

		# dfs starting with root
		dfs(root)

		ans = float("inf")

		for i in range(1, len(values)):
			ans = min(ans, values[i] - values[i-1])

		return ans 



