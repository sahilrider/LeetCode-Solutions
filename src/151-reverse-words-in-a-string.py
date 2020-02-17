'''https://leetcode.com/problems/reverse-words-in-a-string/'''

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = s[::-1]
        return ' '.join(s)
        