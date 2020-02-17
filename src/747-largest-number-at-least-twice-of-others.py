'''https://leetcode.com/problems/largest-number-at-least-twice-of-others/'''

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        for i in nums:
            # print(i, m/2)
            if i!=m and i>m/2:
                return -1
        return nums.index(m)
        