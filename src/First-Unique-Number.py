'''https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3313/'''

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = []
        self.d = {}
        for i in nums:
            if i not in self.d:
                self.d[i] = True    #True means number is in the queue and is unque
                self.q.append(i)
            else:
                if self.d[i] == True:   
                    self.q.remove(i)
                    self.d[i] = False   #False means number was seen but is not unique
        

    def showFirstUnique(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return -1
        

    def add(self, value: int) -> None:
        if value in self.d:
            if self.d[value] == True:
                    self.q.remove(value)
                    self.d[value] = False
        else:
            self.d[value] = True
            self.q.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)