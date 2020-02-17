'''https://leetcode.com/problems/n-queens-ii/'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0]*n for _ in range(n)]
        
        def placeQ(row, col):
            board[row][col] = 1
            
        def removeQ(row, col):
            board[row][col] = 0
            
        def check(row, col):
            for i in range(n):
                if board[row][i]==1:
                    return False
                if board[i][col]==1:
                    return False
            i, j  =row, col
            while i<n and j<n:
                if board[i][j]==1:
                    return False
                i+=1
                j+=1
            i,j = row, col
            while i>-1 and j<n:
                if board[i][j]==1:
                    return False
                i-=1
                j+=1
            i, j = row, col 
            while i>-1 and j>-1:
                if board[i][j]==1:
                    return False
                i-=1
                j-=1
            i, j = row, col 
            while i<n and j>-1:
                if board[i][j]==1:
                    return False
                i+=1
                j-=1
            return True
                
            
        def backtrack(row=0, count=0):
            for col in range(n):
                if check(row, col):
                    placeQ(row, col)
                    if row+1==n:
                        count+=1
                    else:
                        count = backtrack(row+1, count)
                removeQ(row, col)
            return count
        
        return backtrack()
        