'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock/'''

#Approach1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        maxProfit = 0
        for i in prices:
            if minPrice>i:
                minPrice = i
            elif i-minPrice > maxProfit:
                maxProfit = i-minPrice
        return maxProfit

#Approach2
#Kadane's Algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxCur = 0
        maxSoFar = 0
        for i in range(1, len(prices)):
            maxCur = max(0, maxCur + prices[i]-prices[i-1])
            maxSoFar = max(maxCur, maxSoFar)
        return maxSoFar