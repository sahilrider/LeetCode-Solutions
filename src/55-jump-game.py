'''https://leetcode.com/problems/jump-game/'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastpos  = n-1
        for i in range(n-1, -1, -1):
            if i+nums[i] >=lastpos:
                lastpos = i
                
        return lastpos==0