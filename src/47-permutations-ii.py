'''https://leetcode.com/problems/permutations-ii/'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def backtrack(l, rem):
            if not l:
                res.add(tuple(rem))
                return
            for i in range(len(l)):
                backtrack(l[:i]+l[i+1:], rem+[l[i]])
        backtrack(nums, [])
        return list(res)
        