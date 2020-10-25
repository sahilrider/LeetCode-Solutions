'''https://leetcode.com/problems/rotate-array/'''

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k % n
#         nums[:] = nums[n-k:] + nums[:n-k]
#         # print(nums)

# rotate array
# rotate first k
# rotate last n-k 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[::-1]
        print(nums)
        nums[:] = nums[:k][::-1] + nums[k:][::-1]
        print(nums)
        
        