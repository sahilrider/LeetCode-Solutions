'''https://leetcode.com/problems/first-unique-character-in-a-string/'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = []
        d = {}
        for i, val in enumerate(s):
            if val not in d:
                a.append(val)
                d[val] = i
            elif val in d:
                if d[val] is  None:
                    pass
                else:
                    a.remove(val)
                    d[val] = None
            # print(i, val, d, a)
        # print(d, a)
        return d[a[0]] if len(a)>0 else -1