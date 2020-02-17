'''https://leetcode.com/problems/set-matrix-zeroes/'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        erase_row, erase_column = False, False
        if matrix[0][0] == 0:
            erase_row, erase_column = True, True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i==0:
                        erase_row = True
                    if j==0:
                        erase_column = True
                    
        # for j in range(1, len(matrix[0])):
        #     if matrix[0][j]==0:
        #         for i in range(1, len(matrix)):
        #             matrix[i][j]=0
        # for i in range(1, len(matrix)):
        #     if matrix[i][0]==0:
        #         for j in range(1, len(matrix[0])):
        #             matrix[i][j]=0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
        
        if erase_column:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if erase_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
                    
        