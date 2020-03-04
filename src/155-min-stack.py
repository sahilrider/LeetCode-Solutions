'''https://leetcode.com/problems/min-stack/'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []
        self.topp = -1
        

    def push(self, x: int) -> None:
        if self.topp==-1:
            self.topp+=1
            self.stack.append(x)
            self.minstack.append(x)
        else:
            self.topp+=1
            self.stack.append(x)
            self.minstack.append(min(x, self.minstack[self.topp-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        self.topp-=1
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

