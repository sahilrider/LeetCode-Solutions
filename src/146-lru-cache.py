'''https://leetcode.com/problems/lru-cache/'''

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = []
        self.d =  {}

    def get(self, key: int) -> int:
        if key in self.d:
            self.q.remove(key)
            self.q.append(key)
        # print('Get', self.q, self.d)
        return self.d.get(key, -1)
        

    def put(self, key: int, value: int) -> None:
        # print(self.d)
        if key in self.d:
            self.d[key] = value
            self.q.remove(key)
            self.q.append(key)
        else:
            if len(self.q) < self.capacity:
                self.d[key] = value
                self.q.append(key)
            else:
                k = self.q.pop(0)
                del self.d[k]
                self.d[key] = value
                self.q.append(key)
        # print('Put', self.q, self.d)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)