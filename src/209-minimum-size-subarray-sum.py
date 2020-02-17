'''https://leetcode.com/problems/minimum-size-subarray-sum/'''

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, j = 0, 0
        ans = float('inf')
        temp = 0
        while j<len(nums):
            if temp+nums[j]>=s:
                ans = min(ans, j-i+1)
                temp-=nums[i]
                i+=1
            else:
                temp+=nums[j]
                j+=1
        if ans==float('inf'):
            return 0
        else:
            return ans
                