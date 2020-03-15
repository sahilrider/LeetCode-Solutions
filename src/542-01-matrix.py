'''https://leetcode.com/problems/01-matrix/'''

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        newMatrix = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for a in range(len(matrix)):
            for b in range(len(matrix[0])):
                #bfs
                q = [(a,b, 0)]
                visited = []
                while q:
                    # print("Q", q)
                    i, j, step = q.pop(0)
                    if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]) or (i, j) in visited:
                        continue
                    visited.append((i,j))
                    if matrix[i][j]==0:
                        newMatrix[a][b] = step
                        # print(a,b, i, j, newMatrix)
                        break
                    else:
                        q.append((i-1, j, step+1))
                        q.append((i+1, j, step+1))
                        q.append((i, j-1, step+1))
                        q.append((i, j+1, step+1))
        return newMatrix
        