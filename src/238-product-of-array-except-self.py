'''https://leetcode.com/problems/product-of-array-except-self/'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [1]*l
        for i in range(1, l):
            ans[i] = ans[i-1]*nums[i-1]
        # print(ans)
        R = 1
        for i in range(l-1,-1,-1):
            ans[i] = ans[i]*R
            R = R*nums[i]
        return ans
        