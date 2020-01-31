'''https://leetcode.com/problems/n-queens/'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        def placeQ(row, col):
            board[row][col] = 'Q'
            
        def removeQ(row, col):
            board[row][col] = '.'
        
        def display(board):
            res = []
            for rows in board:
                res.append(''.join(rows))
            return res

        def check(row, col):
            for i in range(n):
                if board[row][i]=='Q':
                    return False
                if board[i][col]=='Q':
                    return False
            i, j  =row, col
            while i<n and j<n:
                if board[i][j]=='Q':
                    return False
                i+=1
                j+=1
            i,j = row, col
            while i>-1 and j<n:
                if board[i][j]=='Q':
                    return False
                i-=1
                j+=1
            i, j = row, col 
            while i>-1 and j>-1:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1
            i, j = row, col 
            while i<n and j>-1:
                if board[i][j]=='Q':
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
                        # print(board)
                        ans.append(display(board))
                    else:
                        count = backtrack(row+1, count)
                removeQ(row, col)
            return count
        
        backtrack()
        return ans
