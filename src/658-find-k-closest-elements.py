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
# O(logn + k)
# binary search
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, h = 0, len(arr)-k
        while l<h:
            m = (l+h)//2
            if x - arr[m] > arr[m+k] - x:
                l = m+1
            else:
                h = m
        return arr[l:l+k]

#Solution 3
#Two pointer solution
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, h = 0, len(arr)-1
        while h-l+1>k:
            if abs(arr[h]-x) >= abs(arr[l]-x):
                h-=1
            else:
                l+=1
        return arr[l:h+1]