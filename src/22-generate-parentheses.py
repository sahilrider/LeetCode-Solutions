'''https://leetcode.com/problems/generate-parentheses/'''

#iterative solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [("(", 1, 0)]
        while stack:
            x, l, r = stack.pop()
            if r>l or l>n or r>n:
                continue
            if l==n and r==n:
                res.append(x)
            stack.append((x+"(", l+1, r))
            stack.append((x+")", l, r+1))
        return res

#recursive solution
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
        