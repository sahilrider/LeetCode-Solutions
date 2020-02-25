'''https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        while l<h:
            m = (l+h)//2
            print(l,h,m)
            if nums[m]>nums[h]:
            	'''right part is distrupted
            	   so min should be in [l+1,h]'''
                l = m+1
            elif nums[m]<nums[h]:
            	'''right part is not distrupted
            	   so min should be in [l,h]'''
                h = m
            else:
            	'''nums[m]==nums[h]
            	   duplicate elements'''
                if h!=0 and nums[h-1]>nums[h]:
                	'''indicate h is pivot or min element'''
                    return nums[h]
                else:
                	'''no idea where to check
                	   so decrease h by 1'''
                    h-=1
        # print(l, nums[l])
        return nums[l]