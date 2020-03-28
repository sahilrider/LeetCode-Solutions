'''https://leetcode.com/problems/delete-node-in-a-bst/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def f(self, root):
        parent = root
        node = root.right
        if not node.left:
            return node
        while node.left:
            parent = node
            node = node.left
        parent.left = None if not node.right else node.right
        return node
            
        
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return
        if root.val==key:
            if not root.left and not root.right:
                return None
            if root.left and root.right:
                #inorder successor
                l = root.left
                r = root.right
                root = self.f(root)
                root.left = l
                root.right = r if root is not r else r.right
                return root
                #################
            if root.left:
                return root.left
            if root.right:
                return root.right
        elif root.val>key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
        