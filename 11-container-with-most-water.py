'''https://leetcode.com/problems/container-with-most-water/'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        ans = 0
        while(l<r):
            w = r-l
            h = min(height[l], height[r])
            area = w*h
            if area>ans:
                ans = area
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans
        