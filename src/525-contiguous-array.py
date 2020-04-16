'''https://leetcode.com/problems/contiguous-array/'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ctr = 0
        d = {0:0}
        maxlen = 0
        for i, val in enumerate(nums, 1):
            if val==0:
                ctr-=1
            else:
                ctr+=1
            
            if ctr in d:
                maxlen = max(maxlen, i-d[ctr])
            else:
                d[ctr] = i
        # print(d)
        return maxlen