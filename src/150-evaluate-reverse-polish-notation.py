'''https://leetcode.com/problems/evaluate-reverse-polish-notation/'''

import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+':operator.add, '-':operator.sub , '*':operator.mul , '/':operator.truediv}
        for i in tokens:
            if i not in op:
                stack.append(int(i))
            else:
                # print(stack)
                val2 = stack.pop()
                val1 = stack.pop()
                res = int(op[i](val1, val2))
                stack.append(res)
        return stack[-1]
        