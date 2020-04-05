'''https://leetcode.com/problems/single-number/'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return
        res = nums[0]
        for i in nums[1:]:
            res = res ^ i
        return res
        