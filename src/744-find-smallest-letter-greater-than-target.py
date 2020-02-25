'''https://leetcode.com/problems/find-smallest-letter-greater-than-target/'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, h = 0, len(letters)-1
        while l<h:
            m = (l+h)//2
            if letters[m]>target:
                h = m
            else:
                l = m+1
        if l==len(letters)-1 and letters[l]<=target:
            return letters[0]
        else:
            return letters[l]
        