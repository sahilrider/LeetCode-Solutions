'''https://leetcode.com/problems/sort-colors/'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero, one, two = 0, 0, n-1
        
        while one<=two:
            if nums[one]==0:
                nums[zero], nums[one] = nums[one], nums[zero]
                zero+=1
                one+=1
            elif nums[one]==1:
                one+=1
            else:
                nums[one], nums[two] = nums[two], nums[one]
                two-=1
                