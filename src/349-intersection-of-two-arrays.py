'''https://leetcode.com/problems/intersection-of-two-arrays/'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = set(nums1), set(nums2)
        return list(a.intersection(b))