'''https://leetcode.com/problems/letter-combinations-of-a-phone-number/'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        
        res = []
        n = len(digits)
        if n==0:
            return []
        
        def backtrack(ans='', idx=0):
            if idx==n:
                res.append(ans)
                return
            for i in mapping[digits[idx]]:
                backtrack(ans+i, idx+1)
        backtrack()
        return res
        