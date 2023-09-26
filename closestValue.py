"""
Closest Binary Search Tree Value

Given the root of a binary search tree and a target value, 

return the value in the BST 

that is closest to the target. 

If there are multiple answers, print the smallest.
"""

# Definition for a binary tree node 
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val 
		self.left = left 
		self.right = right 

# Binary search, O(H) 
# go left if target is smaller than current root value 
# go right otherwise 
# choose the closest to target value at each step 
class Solution:
	def closestValue(self, root: Optional[TreeNode], target: float)-> int:
		closest = root.val 

		while  root:
			closest = min(root.val, closest, key=lambda x: (abs(target - x), x))

			root = root.left if target < root.val else root.right 

		return closest






















