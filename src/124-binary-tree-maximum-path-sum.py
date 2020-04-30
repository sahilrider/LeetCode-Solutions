'''https://leetcode.com/problems/binary-tree-maximum-path-sum/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.max = max(self.max, l+node.val+r)
            return max(0, node.val+max(l,r))
        self.max = float('-inf')
        dfs(root)
        return self.max
        