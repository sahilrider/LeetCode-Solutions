'''https://leetcode.com/problems/same-tree/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val==q.val:
                return True
            else:
                return False
            
        l = list()
        l.append([p,q])
        while l:
            p, q = l.pop(0)
            if not check(p,q):
                return False
            if p:
                l.append([p.left, q.left])
                l.append([p.right, q.right])
        return True
        