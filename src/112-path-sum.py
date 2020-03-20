'''https://leetcode.com/problems/path-sum/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, summ: int) -> bool:
        
        def traverse(root, tempSum, totalsum):
            # print(root.val)
            if root.left is None and root.right is None:
                if tempSum+root.val==totalsum:
                    return True
                else:
                    return False
            if root.left and root.right:
                return traverse(root.left, tempSum+root.val, summ) or traverse(root.right, tempSum+root.val, summ)
            if root.left:
                return traverse(root.left, tempSum+root.val, summ)
            if root.right:
                return traverse(root.right, tempSum+root.val, summ)
            
        if not root:
            return False
        return traverse(root, 0, summ)
        