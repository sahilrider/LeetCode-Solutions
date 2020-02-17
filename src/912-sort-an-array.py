'''https://leetcode.com/problems/sort-an-array/'''

class Solution:
    def merge(self, left, right):
        l, r = 0, 0
        res = []
        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                res.append(left[l])
                l+=1
            else:
                res.append(right[r])
                r+=1
        while l<len(left):
            res.append(left[l])
            l+=1
        while r<len(right):
            res.append(right[r])
            r+=1
        return res
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        
        pivot = len(nums)//2
        
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        return self.merge(left, right)
        