'''https://leetcode.com/problems/longest-palindromic-substring/'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s)<1:
            return ""
        l = len(s)
        low, high = 0, 0
        start = 0
        maxlen = 1
        for i in range(1,l):
            low = i-1
            high = i
            while low>=0 and high<l and s[low]==s[high]:
                # print(i, low, high, s[low], s[high])
                if high-low+1 > maxlen:
                    start = low
                    maxlen = high-low+1
                low-=1
                high+=1
            
            low, high = i-1, i+1
            while low>=0 and high<l and s[low]==s[high]:
                # print(i, low, high, s[low], s[high])
                if high-low+1 > maxlen:
                    start = low
                    maxlen = high-low+1
                low-=1
                high+=1
        return s[start:start+maxlen]
        