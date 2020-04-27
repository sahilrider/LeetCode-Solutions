'''https://leetcode.com/problems/maximal-square/'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        ans = 0
        n, m = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[0][i] == '1':
                ans = 1
                break
        for i in range(n):
            if matrix[i][0] == '1':
                ans = 1
                break
        # print(matrix)
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == '1':
                    matrix[i][j] = min(int(matrix[i-1][j-1]), int(matrix[i-1][j]), int(matrix[i][j-1])) + 1
                    ans = max(ans, matrix[i][j])
                # print(matrix)
        return ans**2
        