'''https://leetcode.com/problems/reverse-integer/'''

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        neg = 0
        if x[0] =='-':
            neg = 1
            n = x[1:]
            n = n[::-1]
            ans = -1*int(n)
        else:
            n = x[::-1]
            ans = int(n)
        if ans>=(-2**31) and ans<=(2**31 - 1):
            return ans
        else:
            return 0
        