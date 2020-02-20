'''https://leetcode.com/problems/sqrtx/'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        l, h = 1, x
        while h-l!=1:
            m = (l+h)//2
            # print(l, h, m)
            if m*m == x:
                return m
            elif m*m > x:
                h = m
            else:
                l = m
        return l