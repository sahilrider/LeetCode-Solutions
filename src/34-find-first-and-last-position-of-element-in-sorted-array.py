'''https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(n):
            l, h = 0, len(nums)
            while l<h:
                m = (l+h)//2
                if nums[m]>=n:
                    h = m
                else:
                    l = m+1
            return l
        left = search(target)
        if target in nums[left:left+1]:
            return [left, search(target+1)-1]
        else:
            return [-1, -1]