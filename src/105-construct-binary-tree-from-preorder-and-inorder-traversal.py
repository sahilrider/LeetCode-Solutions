'''https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def build(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        rootval = preorder.pop(0)
        # print(rootval)
        idx = inorder.index(rootval)
        left = inorder[:idx]
        right = inorder[idx+1:]
        root = TreeNode(rootval)
        root.left = self.build(preorder, left)
        root.right = self.build(preorder, right)
        # print(root)
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        return self.build(preorder, inorder)