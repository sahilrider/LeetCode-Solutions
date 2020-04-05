'''https://leetcode.com/problems/happy-number/'''

class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while True:
            if n == 1:
                return True
            elif n in d:
                return False
            else:
                d[n] = 1
                n = sum(int(i)**2 for i in str(n))
        