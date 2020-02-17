'''https://leetcode.com/problems/3sum/'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        l = len(nums)
        nums.sort()
        for i in range(l):
            if i>1 and nums[i]==nums[i-1]:
                continue
            d = {}
            for j in range(i+1, l):
                diff = 0 - nums[i] - nums[j]
                if diff not in d:
                    d[nums[j]] = j
                else:
                    t = (nums[i], nums[j], nums[d[diff]])
                    ans.add(t)
        # print(ans)
        return ans