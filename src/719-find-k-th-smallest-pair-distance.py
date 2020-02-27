'''https://leetcode.com/problems/find-k-th-smallest-pair-distance/'''

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, h = 0, nums[-1]-nums[0]
        
        while l<h:
            mid = (l+h)//2
            
            i, j = 0, 0
            count = 0
            while i<n:
                while j<n and nums[j]-nums[i]<=mid:
                    j+=1
                count += j-i-1
                i+=1
            if count>=k:
                h = mid
            else:
                l = mid+1
        return l
        