'''https://leetcode.com/problems/two-sum/'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff not in d:
                d[val] = i
            else:
                return [d[diff], i]
        