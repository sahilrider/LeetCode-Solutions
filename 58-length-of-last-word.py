'''https://leetcode.com/problems/length-of-last-word/'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        try:
            return len(l[-1])
        except:
            return 0
        