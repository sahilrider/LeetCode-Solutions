'''https://leetcode.com/problems/reverse-words-in-a-string-iii/'''

# reverse each word
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = []
        for i in s:
            ans.append(i[::-1])
        return ' '.join(ans)

# reverse the whole string and split and then reverse again
# reverse the order of the words and then reverse the entire string.
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        s = s.split()
        s = s[::-1]
        return ' '.join(s)
        