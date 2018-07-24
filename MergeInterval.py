# Leetcode: https://leetcode.com/problems/merge-intervals/description/


# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        rs = []
        if not intervals:
            return rs
        intervals.sort(key = lambda interval: -interval.start)  # descending order sort -> Then pop will be O(1) space.
        initInterval = intervals.pop()
        start = initInterval.start
        end = initInterval.end
        while intervals:
            newInterval = intervals.pop()
            if end < newInterval.start:
                rs.append([start, end])
                start = newInterval.start
                end = newInterval.end
            else:
                end = max(end, newInterval.end)
        
        rs.append([start, end])
        
        return rs   