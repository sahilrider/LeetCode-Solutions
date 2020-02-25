'''https://leetcode.com/problems/valid-perfect-square/'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, h = 1, num
        while l<=h:
            m = (l+h)//2
            if m*m==num:
                return True
            elif m*m>num:
                h = m-1
            else:
                l = m+1
        return False
        