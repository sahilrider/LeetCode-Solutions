'''https://leetcode.com/problems/plus-one/'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        ans = []
        c = 1
        for d in digits:
            t = d+c
            if t>9:
                t = t-10
                c=1
            else:
                c=0
            ans.append(t)
        if c:
            ans.append(1)
        return reversed(ans)
            
        