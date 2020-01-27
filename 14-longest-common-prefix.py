'''https://leetcode.com/problems/longest-common-prefix/'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==[]:
            return ''
        n = [len(s) for s in strs]
        res =''
        for i in range(min(n)):
            target = strs[0][i]
            for s in strs[1:]:
                if s[i]!=target:
                    return res
            res = res+target
        return res