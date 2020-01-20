'''https://leetcode.com/problems/jump-game-ii/'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        n , start, end, step = len(nums), 0, 0, 0
        maxend = 0
        while end< n-1:
            step +=1
            for i in range(start, end+1):
                maxend = max(maxend, i+nums[i])
                if maxend >= n-1:
                    return step
            start, end = end+1 , maxend
        return 0 if n==1 else -1
                    
            
            
        