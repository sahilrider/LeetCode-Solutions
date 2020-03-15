'''https://leetcode.com/problems/flood-fill/'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = []
        target = image[sr][sc]
        def dfs(i, j):
            if i<0 or j<0 or i>=len(image) or j>=len(image[0]) or (i,j) in visited:
                return
            # print(visited)
            visited.append((i,j))
            if image[i][j]==target:
                image[i][j] = newColor
                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i-1, j)
                dfs(i+1, j)
        dfs(sr, sc)
        return image
        