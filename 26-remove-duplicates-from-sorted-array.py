'''https://leetcode.com/problems/remove-duplicates-from-sorted-array/'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        ans = 0
        for i in range(1, l):
            if nums[i]!=nums[ans]:
                ans+=1
                nums[i], nums[ans] = nums[ans], nums[i]
        return ans+1