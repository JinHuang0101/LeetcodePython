"""
Example 1: 938. Range Sum of BST

Given the root node of a binary search tree and two integers 

low and high, 

return the sum of values of all nodes 

with a value in the inclusive range [low, high].
"""

class Solution:
	def rangeSumBST(self, root: Optional[TreeNode], low:int, high: int)->int:
		if not root:
			return 0 


		ans = 0 

		if low <= root.val <= high:
			ans += root.val 

		# to the left
		if low < root.val:
			ans += self.rangeSumBST(root.left, low, high)

		# to the right
		if root.val < high:
			ans += self.rangeSumBST(root.right, low, high)


		return ans