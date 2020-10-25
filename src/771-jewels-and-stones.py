'''https://leetcode.com/problems/jewels-and-stones/'''

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = list(J)
        ans = 0
        for i in S:
            if i in J:
                ans+=1
        return ans
        