'''https://leetcode.com/problems/open-the-lock/'''

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        moved = set(deadends)
        if '0000' in moved:
            return -1
        q = ['0000']
        count = 0
        moves = {str(i): [str((i+1)%10), str((i-1)%10)] for i in range(10)}
        while q:
            new = []
            count +=1
            for s in q:
                for i, c in enumerate(s):
                    for curr in (s[:i]+moves[c][0]+s[i+1:], s[:i]+moves[c][1]+s[i+1:]):
                        if curr not in moved:
                            if curr==target:
                                return count
                            new.append(curr)
                            moved.add(curr)
            q = new
        return -1
            
        