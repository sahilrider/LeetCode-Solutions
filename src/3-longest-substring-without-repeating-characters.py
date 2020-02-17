'''https://leetcode.com/problems/longest-substring-without-repeating-characters/'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        ans = 0
        i = 0
        for j, val in enumerate(s):
            if val not in d:
                ans = max(ans, j-i+1)
                d[val] = j+1
            else:
                i = max(i, d[val])
                d[val] = j+1
                ans = max(ans, j-i+1)
        return ans