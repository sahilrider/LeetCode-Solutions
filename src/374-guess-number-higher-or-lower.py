'''https://leetcode.com/problems/guess-number-higher-or-lower/'''

# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, n
        while l<=h:
            m = (l+h)//2
            if guess(m)==0:
                return m
            elif guess(m)==1:
                l = m+1
            else:
                h = m-1
        