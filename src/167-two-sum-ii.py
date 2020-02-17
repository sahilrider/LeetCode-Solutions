'''https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, h = 0, len(numbers)-1
        while l<h:
            if numbers[l]+numbers[h] == target:
                return [l+1, h+1]
            elif numbers[l]+numbers[h] > target:
                h-=1
            else:
                l+=1
                
        