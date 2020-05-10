'''https://leetcode.com/problems/ransom-note/'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for l in magazine:
            d[l] = d.get(l, 0)+1
        
        for l in ransomNote:
            if l not in d or d[l]<=0:
                return False
            else:
                d[l] -=1
        return True