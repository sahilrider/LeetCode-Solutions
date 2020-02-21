'''https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/'''

#solution 1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        while l<h:
            m = (l+h)//2
            if nums[m]>=nums[l]:
                '''left side is sorted
                    smallest element is nums[l] in this subarray'''
                if nums[m]<=nums[h]:
                    h = m
                else:
                    l = m+1
            else:
                #left side is not sorted
                h = m
        return nums[l]

#solution 2

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        while l<h:
            m = (l+h)//2
            if nums[m]>=nums[h]:
                l = m+1
            else:
                h = m
        return nums[l]