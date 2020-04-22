'''https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3306/'''

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        i, j = 0, m-1
        ans = float('inf')
        while i<n and j>=0:
            p = binaryMatrix.get(i,j)
            if p==0:
                i+=1
            else:
                ans = min(ans, j)
                j-=1
        if ans==float('inf'):
            return -1
        else:
            return ans