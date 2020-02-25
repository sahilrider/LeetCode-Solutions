'''https://leetcode.com/problems/intersection-of-two-arrays-ii/'''

#Solution 1
#Brute Force
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            return self.intersect(nums2, nums1)
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
        return res
        

#Solution 2
#Using Counter
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            return self.intersect(nums2, nums1)
        res = []
        c = Counter(nums1)
        # print(c)
        for i in nums2:
            if c[i]>0:
                res.append(i)
                c[i]-=1
                # print(c)
        return res
        