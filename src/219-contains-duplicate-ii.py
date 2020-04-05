'''https://leetcode.com/problems/contains-duplicate-ii/'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, val in enumerate(nums):
            if val not in d:
                d[val] = i
            else:
                res = i - d[val]
                if res<=k:
                    return True
                d[val] = i
        return False
        