'''https://leetcode.com/problems/insert-into-a-binary-search-tree/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#iterative solution
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        it = root
        while it:
            parent = it
            if val>it.val:
                it = it.right
            else:
                it = it.left
        if val>parent.val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
        return root

#recursive solution
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val>root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root        