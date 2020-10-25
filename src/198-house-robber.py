'''https://leetcode.com/problems/house-robber/'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = second
            second = max(first+nums[i], second)
            first = temp
        return second