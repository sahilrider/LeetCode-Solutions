'''https://leetcode.com/problems/maximum-subarray/'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tempmax, allmax = nums[0], nums[0]
        n = len(nums)
        for i in range(1,n):
            tempmax = max(nums[i], tempmax+nums[i])
            if tempmax>allmax:
                allmax = tempmax
        return allmax
        