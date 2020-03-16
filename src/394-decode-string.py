'''https://leetcode.com/problems/decode-string/'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curStr = ''
        for i in s:
            if i=='[':
                stack.append(curStr)
                stack.append(curNum)
                curNum = 0
                curStr = ''
            elif i==']':
                num = stack.pop()
                prevStr = stack.pop()
                curStr = prevStr + num*curStr
            elif i.isdigit():
                curNum = curNum*10 + int(i)
            else:
                curStr +=i
        return curStr
        