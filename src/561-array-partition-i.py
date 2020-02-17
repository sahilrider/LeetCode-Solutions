'''https://leetcode.com/problems/array-partition-i/'''

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in nums[::2]:
            res+=i
        return res
        