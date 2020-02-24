'''https://leetcode.com/problems/find-k-closest-elements/'''

#solution 1
# O(nlogn)
#Get absolute diff, sort and get the first k elements
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        b = []
        for i in arr:
            b.append(abs(i-x))
        c = [x for _,x in sorted(zip(b, arr))]
        return sorted(c[:k])
        
# solution 2
# O(logn)
# binary search
