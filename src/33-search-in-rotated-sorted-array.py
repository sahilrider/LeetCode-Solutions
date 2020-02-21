'''https://leetcode.com/problems/search-in-rotated-sorted-array/'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while l<=h:
            mid = l + (h-l)//2
            if nums[mid]==target:
                return mid
            
            if nums[mid]>=nums[l]:   #left part is sorted
                if target>=nums[l] and target<=nums[mid]:
                    h = mid-1
                else:
                    l = mid+1
            else:   #right part is sorted
                if target>=nums[mid] and target<=nums[h]:
                    l = mid+1
                else:
                    h = mid-1
        return -1
            