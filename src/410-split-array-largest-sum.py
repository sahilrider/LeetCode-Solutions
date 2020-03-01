'''https://leetcode.com/problems/split-array-largest-sum/'''

class Solution:
    def valid(self, nums, cuts, maxx):
        acc = 0
        for num in nums:
            if num>maxx:
                return False
            elif acc+num<=maxx:
                acc+=num
            else:
                cuts-=1
                acc = num
                if cuts<0:
                    return False
        return True
    
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while l<r:
            mid = (l+r)//2
            if self.valid(nums, m-1, mid):
                r = mid
            else:
                l = mid+1
        return l
        