'''https://leetcode.com/problems/search-in-a-binary-search-tree/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        while root:
            if root.val==val:
                return root
            elif root.val>val:
                root = root.left
            else:
                root = root.right
        return None
        