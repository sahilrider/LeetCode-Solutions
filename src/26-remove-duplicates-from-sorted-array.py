'''https://leetcode.com/problems/remove-duplicates-from-sorted-array/'''

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         l = len(nums)
#         ans = 0
#         for i in range(1, l):
#             if nums[i]!=nums[ans]:
#                 ans+=1
#                 nums[i], nums[ans] = nums[ans], nums[i]
#         return ans+1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        p1, p2 = 0, 1 
        while p2<len(nums):
            if nums[p2]!=nums[p1]:
                p1+=1
                nums[p1] = nums[p2]
            p2+=1
        return p1+1
        