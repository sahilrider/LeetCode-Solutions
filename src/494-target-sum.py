'''https://leetcode.com/problems/target-sum/'''

#Solution 1
#Recursion
#TLE
class Solution:
    count = 0
    def calculate(self, nums, i, tempsum, S):
        if i==len(nums):
            if tempsum==S:
                # print('Y')
                self.count+=1
        else:
            self.calculate(nums, i+1, tempsum+nums[i], S)
            self.calculate(nums, i+1, tempsum-nums[i], S)
            
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.calculate(nums, 0, 0, S)
        return self.count
        
#Solution 2
#DP
#Accepted
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        dp = {0:1}
        for i in nums:
            temp = {}
            for d in dp.keys():
                # print(i, d, dp[d])
                temp[d+i] = dp.get(d, 0) + temp.get(d+i, 0)
                temp[d-i] = dp.get(d, 0) + temp.get(d-i, 0)
            dp = temp
            print(dp)
        return dp.get(S, 0)
        
        