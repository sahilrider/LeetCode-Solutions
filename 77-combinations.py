'''https://leetcode.com/problems/combinations/'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = set()
        def isvalid(temp, i):
            if not temp:
                return True
            if i>temp[-1]:
                return True
            return False
        
        def backtrack(temp=[], start=1):
            for i in range(start, n+1):
                if isvalid(temp, i):
                    temp = temp +[i]
                    if len(temp)==k:
                        # print(temp)
                        res.add(tuple(temp))
                    else:
                        backtrack(temp, start+1)
                    if temp:
                        temp.pop()
        backtrack()
        return res
        