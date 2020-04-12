'''https://leetcode.com/problems/diameter-of-binary-tree/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.ans = 1
        def depth(root):
            if not root:
                return 0
            left, right = depth(root.left), depth(root.right)
            self.ans = max(self.ans, left+right+1)
            return max(left, right)+1
        depth(root)
        return self.ans-1
        