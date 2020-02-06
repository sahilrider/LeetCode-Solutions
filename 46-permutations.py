'''https://leetcode.com/problems/permutations/'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(l, rem):
            if not l:
                res.append(rem)
                return
            for i in range(len(l)):
                backtrack(l[:i]+l[i+1:], rem+[l[i]])
        backtrack(nums, [])
        return res
        