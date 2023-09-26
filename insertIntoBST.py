"""
Insert into a Binary Search Tree

You are given the root node of a binary search tree (BST) 

and a value to insert into the tree. 

Return the root node of the BST after the insertion. 

It is guaranteed that the new value does not exist 

in the original BST.

Notice that there may exist multiple valid ways 

for the insertion, as long as the tree remains a BST 

after insertion. You can return any of them.
"""

# recursion 
# O(H) where H is a tree height 
# O(logN) average case, O(N) worst case 
class Solution:

	def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

		# if empty tree
		# just insert this new node 
		if not root:
			return TreeNode(val)

		# insert into the right subtree 
		if val > root.val:
			root.right = self.insertIntoBST(root.right, val)
		
		# insert into the left subtree
		else:
			root.left = self.insertIntoBST(root.left, val)

		return root 



























