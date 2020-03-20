'''https://leetcode.com/problems/symmetric-tree/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val==right.val:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        else:
            return False
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
        