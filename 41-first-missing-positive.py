'''https://leetcode.com/problems/first-missing-positive/'''

#time - O(n)
#space - O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i<n:
            if nums[i]>0 and nums[i]<=n and nums[i]!=nums[nums[i]-1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1

#time - O(n)
#space - O(n)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        l = [None]*n
        for i in nums:
            if i>=1 and i<=n:
                l[i-1] = 1
        for i in range(n):
            if l[i] is None:
                return i+1
        return n+1