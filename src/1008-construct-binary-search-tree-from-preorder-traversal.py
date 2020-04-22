'''https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        stack = []
        root = TreeNode(preorder.pop(0))
        stack.append(root)
        while preorder:
            node = TreeNode(preorder.pop(0))
            if node.val<stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and stack[-1].val<node.val:
                    last = stack.pop()
                last.right = node
                stack.append(last.right)
        return root
        