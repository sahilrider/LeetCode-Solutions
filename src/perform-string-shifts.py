'''https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3299/'''

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if not s:
            return s
        rightshift = 0
        s = list(s)
        for i in shift:
            if i[0]==1: #right
                rightshift+=i[1]
            else:
                rightshift-=i[1]
        ########
        # Now shift
        rightshift %=len(s)
        ans = s[-rightshift:] + s[:-rightshift]
        return ''.join(ans)
        