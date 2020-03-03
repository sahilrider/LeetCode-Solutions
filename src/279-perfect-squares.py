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
    
        