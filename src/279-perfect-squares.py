'''https://leetcode.com/problems/perfect-squares/'''

#Solution1
#Recursion
#TLE
class Solution:
    def numSquares(self, n: int) -> int:
        #finding all squares till n
        squares = [i*i for i in range(1,int(n**0.5)+1)]
        squares = squares[::-1]
        print(squares)
        #dfs to find the solution
        def f(n, step=0):
            if n<0:
                return float('inf')
            if n==0:
                return step
            return min(f(n-s, step+1) for s in squares)
        
        return f(n, 0)
                
#Solution2
#BFS   
#Accepted
class Solution:
    def numSquares(self, n: int) -> int:
        #finding all squares till n
        squares = [i*i for i in range(1,int(n**0.5)+1)]
        squares = squares[::-1]
        q = [n]
        step = 0
        while q:
            # print(step, q)
            step+=1
            new = []
            for val in q:
                for square in squares:
                    if val-square==0:
                        return step
                    if val-square>0:
                        new.append(val-square)
            q = new
        
#Solution3
#DP
#Accepted
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[1] = 1
        perfect = [1]
        for i in range(2, n+1):
            if (i**0.5 - int(i**0.5))==0:   #perfect square
                perfect.append(i)
                dp[i] = 1
            else:
                dp[i] = min(dp[i], min(dp[i-j] for j in perfect)+1)
        return dp[n]
        
            
        