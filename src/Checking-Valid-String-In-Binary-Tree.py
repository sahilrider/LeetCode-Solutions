'''https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(node, seq):
            if not node.left and not node.right:
                if seq + [node.val] == self.arr:
                    return True
                else:
                    return False
            if node.left and node.right:
                return dfs(node.left, seq+[node.val]) or dfs(node.right, seq+[node.val])
            if node.left:
                return dfs(node.left, seq+[node.val])
            if node.right:
                return dfs(node.right, seq+[node.val])
        self.arr = arr
        if not root:
            return False
        return dfs(root, [])
        