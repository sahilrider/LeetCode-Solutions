'''https://leetcode.com/problems/majority-element/'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thres = len(nums)//2
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for k, val in d.items():
            if val>thres:
                return k
        