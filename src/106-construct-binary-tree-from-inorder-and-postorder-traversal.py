'''https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def build(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        rootval = postorder.pop()
        idx = inorder.index(rootval)
        root = TreeNode(rootval)
        root.right = self.build(inorder[idx+1:], postorder)
        root.left = self.build(inorder[:idx], postorder)
        return root
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        return self.build(inorder, postorder)
        