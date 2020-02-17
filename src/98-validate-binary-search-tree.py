'''https://leetcode.com/problems/validate-binary-search-tree/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            val = node.val
            if val<=lower or val>=upper:
                return False
            return helper(node.left, lower, val) and helper(node.right, val, upper)
        
        return helper(root)