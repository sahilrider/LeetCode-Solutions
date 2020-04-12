'''https://leetcode.com/problems/backspace-string-compare/'''

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1 = []
        for i in S:
            if i=='#':
                if s1: s1.pop()
            else:
                s1.append(i)
        s2 = []
        for i in T:
            if i=='#':
                if s2: s2.pop()
            else:
                s2.append(i)
        return s1==s2