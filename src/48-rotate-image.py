'''https://leetcode.com/problems/rotate-image/'''

class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a.reverse()
        n = len(a)
        for i in range(n):
            for j in range(i):
                a[i][j], a[j][i] = a[j][i], a[i][j]
        
        