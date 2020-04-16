'''https://leetcode.com/problems/last-stone-weight/'''

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        stones = [i*-1 for i in stones]
        heapq.heapify(stones)
        while len(stones)>=2:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            val = abs(a)-abs(b)
            if val:
                heapq.heappush(stones, -1*val)
        if stones:
            return stones[0]*-1
        else:
            return 0
        
        