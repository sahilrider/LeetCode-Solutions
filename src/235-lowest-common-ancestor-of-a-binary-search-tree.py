'''https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val>q.val:
            return self.lowestCommonAncestor(root, q, p)
        while root:
            if p.val<=root.val and q.val>=root.val:
                return root
            if p.val<root.val and q.val<root.val:
                root = root.left
            else:
                root = root.right
                
        