'''https://leetcode.com/problems/generate-parentheses/'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(s='', l=0, r=0):
            if len(s)==2*n:
                ans.append(s)
                return
            if l<n:
                backtrack(s+'(', l+1, r)
            if r<l:
                backtrack(s+')', l, r+1)
        backtrack()
        return ans
        