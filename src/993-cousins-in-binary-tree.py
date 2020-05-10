'''https://leetcode.com/problems/cousins-in-binary-tree/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.val_depth = 0
        self.val_parent = None
        def dfs(node, value, depth, parent):
            if not node:
                return
            if node.val == value:
                self.val_depth = depth
                self.val_parent = parent
                return
            else:
                dfs(node.left, value, depth+1, node.val)
                dfs(node.right, value, depth+1, node.val)

        dfs(root, x, 0, None)
        x_depth = self.val_depth
        x_parent = self.val_parent
        
        dfs(root, y, 0, None)
        if x_depth==self.val_depth and x_parent!=self.val_parent:
            return True
        else:
            return False