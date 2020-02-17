'''https://leetcode.com/problems/move-zeroes/'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = -1, 0
        while j<len(nums):
            if nums[j]!=0:
                i+=1
                nums[i], nums[j] = nums[j], nums[i]
            j+=1
                