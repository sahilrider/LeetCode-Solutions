'''https://leetcode.com/problems/binary-tree-preorder-traversal/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Solution1
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while True:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            root = node.right

#Solution2
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                # print(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
        