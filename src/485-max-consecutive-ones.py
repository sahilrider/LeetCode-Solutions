'''https://leetcode.com/problems/max-consecutive-ones/'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i, j = 0, 0
        ans = 0
        while j<len(nums):
            if nums[j]==0:
                ans = max(ans, j-i)
                i = j+1
            j+=1
        return max(ans, j-i)