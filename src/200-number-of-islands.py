'''https://leetcode.com/problems/number-of-islands/'''

#Solution1
#Recursive DFS solution
class Solution:
    def sink(self, grid, i, j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0':
            return 0
        grid[i][j] = '0'
        self.sink(grid, i+1, j)
        self.sink(grid, i-1, j)
        self.sink(grid, i, j+1)
        self.sink(grid, i, j-1)
        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        if grid==[] or grid==[[]]:
            return 0
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    ans+=self.sink(grid, i, j)
                    # print(grid)
        return ans

#Solution2
#Iterative BFS solution
class Solution:
    def sink(self, grid, i, j):
        q = [(i,j)]
        vis = [(i,j)]
        while q:
            a, b = q.pop(0)
            if a+1!=len(grid) and (a+1, b) not in vis and grid[a+1][b]=='1':
                grid[a+1][b] = '0'
                q.append((a+1, b))
                vis.append((a+1, b))
            if b+1!=len(grid[0]) and (a, b+1) not in vis and grid[a][b+1]=='1':
                grid[a][b+1] = '0'
                q.append((a, b+1))
                vis.append((a+1, b))
            if a-1>=0 and (a-1, b) not in vis and grid[a-1][b]=='1':
                grid[a-1][b] = '0'
                q.append((a-1, b))
                vis.append((a-1, b))
            if b-1>=0 and (a, b-1) not in vis and grid[a][b-1]=='1':
                grid[a][b-1] = '0'
                q.append((a, b-1))
                vis.append((a-1, b))

    def numIslands(self, grid: List[List[str]]) -> int:
        if grid==[] or grid==[[]]:
            return 0
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    ans+=1
                    self.sink(grid, i, j)
                    # print(grid)
        return ans