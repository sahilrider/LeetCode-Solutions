'''https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def helper(low, high):
            m = (low+high)//2
            node = TreeNode(nums[m])
            if m-1>=low:
                node.left = helper(low, m-1)
            if m+1<=high:
                node.right = helper(m+1, high)
            return node
        
        if nums is None or len(nums)==0:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        ans = helper( 0, len(nums)-1)
        return ans