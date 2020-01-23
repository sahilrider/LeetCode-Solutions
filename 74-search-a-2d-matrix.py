'''https://leetcode.com/problems/search-a-2d-matrix/'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        rows, cols = len(matrix), len(matrix[0])
        
        l, h = 0, rows*cols-1
        while l<=h:
            m = (l+h)//2
            num = matrix[m//cols][m%cols]
            if num==target:
                return True
            elif num<target:
                l = m+1
            else:
                h = m-1
        return False