'''https://leetcode.com/problems/binary-tree-level-order-traversal/'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        q = list()
        q.append((root, 0))
        res = dict()
        while q:
            node, level = q.pop(0)
            if node:
                res[level] = res.get(level, []) +[node.val]
                q.append((node.left, level+1))
                q.append((node.right,level+1))
        return list(res.values())
        
        