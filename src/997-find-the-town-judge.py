'''https://leetcode.com/problems/find-the-town-judge/'''

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return N
        d = {}
        l = set()
        for i in trust:
            d[i[1]] = d.get(i[1], []) + [i[0]]
            l.add(i[0])
        # print(d)
        for k,v in d.items():
            if len(v)==N-1 and k not in l:
                return k
        return -1