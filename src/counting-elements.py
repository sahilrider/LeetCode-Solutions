'''https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/'''

class Solution:
    def countElements(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0)+1
        ans = 0
        for k in d.keys():
            if k+1 in d:
                ans+=d[k]
        return ans