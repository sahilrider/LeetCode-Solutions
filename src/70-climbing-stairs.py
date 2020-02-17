'''https://leetcode.com/problems/climbing-stairs/'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        f, s = 1, 2
        for i in range(3, n+1):
            ans = f+s
            f, s = s, ans
        return ans
        