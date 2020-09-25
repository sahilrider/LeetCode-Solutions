'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/'''

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         profit = 0 
#         cp = prices[0]
#         for i in prices[1:]:
#             # print(cp)
#             if i<cp:
#                 cp = i
#             elif i>cp:
#                 profit += i-cp
#                 cp = i
#         return profit

#second attempt     
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0 
        cp = prices[0]
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit
        