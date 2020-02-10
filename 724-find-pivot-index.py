'''https://leetcode.com/problems/find-pivot-index/'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        for i, val in enumerate(nums):
            if leftsum == total-leftsum-val:
                return i
            leftsum+=val
        return -1