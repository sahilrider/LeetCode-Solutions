'''https://leetcode.com/problems/insert-interval/'''

#Append new interval and sort

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        intervals.append(newInterval)
        res = []
        intervals.sort()
        start, end = intervals[0][0], intervals[0][1]
        for i in intervals[1:]:
            if i[0]<=end:
                end = max(end, i[1])
            else:
                res.append([start, end])
                start, end = i[0], i[1]
        res.append([start, end])
        return res

#New approach 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for i in intervals:
            if i[1] < s:
                left.append(i)
            elif i[0] > e:
                right.append(i)
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return left + [[s, e]] + right