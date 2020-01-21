'''https://leetcode.com/problems/merge-intervals/'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
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