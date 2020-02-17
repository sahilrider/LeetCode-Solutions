'''https://leetcode.com/problems/unique-paths-ii/'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            if obstacleGrid[0][i]!= 1:
                dp[0][i] = 1
            else:
                break
        for i in range(n):
            if obstacleGrid[i][0]!= 1:
                dp[i][0] = 1
            else:
                break
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j]==1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        