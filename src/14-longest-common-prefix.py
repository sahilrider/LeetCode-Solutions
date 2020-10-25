'''https://leetcode.com/problems/longest-common-prefix/'''

#Vertical scanning
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

#Horizontal Scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = strs[0]
        for s in strs[1:]:
            while s.find(ans)!=0:
                ans = ans[:-1]
                if len(ans)==0:
                    return ""
        return ans

#Divide n Conquer
def commonPrefix(left, right):
    # print(left, right)
    minL = min(len(left), len(right))
    for i in range(minL):
        if left[i]!=right[i]:
            return left[:i]
    return left[:minL]

def helper(strs, l, r):
    # print(strs, l, r)
    if l==r:
        return strs[l]
    else:
        m = (l+r)//2
        lcpLeft = helper(strs, l, m)
        lcpRight = helper(strs, m+1, r)
        return commonPrefix(lcpLeft, lcpRight)
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs)==0:
            return ""
        return helper(strs, 0, len(strs)-1)

#Binary Search
def isCommonPrefix(strs, length):
    prefix = strs[0][:length]
    for s in strs[1:]:
        if s.find(prefix)!=0:
            return False
    return True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        minLen = min(len(s) for s in strs)
        # print(minLen)
        l, h = 0, minLen
        while l<=h:
            m = (l+h)//2
            if isCommonPrefix(strs, m):
                l = m+1
            else:
                h = m-1
        return strs[0][:(l+h)//2]