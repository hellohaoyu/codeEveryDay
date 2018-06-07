# Leetcode: https://leetcode.com/problems/meeting-rooms-ii/description/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# Keys: 1. know to use heapq in python, heapq.heappush(pq, element), heapq.heappop(pq), heapq.heapify([]) 
#       2. len(null) will have problem, please check null before using len
#       3. how to do customize sorting -> intervals.sort(key = lambda interval : interval.start)
#       4. how to get the max/min value of priority queue in python -> min:pq[0], max:pq[-1]

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals): # [[15, 20]]
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals or len(intervals) < 1:
            return 0
        
        rs = 0
        curMeetings = []
        
        intervals.sort(key = lambda interval : interval.start)
        
        while intervals:
            curIn = intervals.pop(0)
            heapq.heappush(curMeetings, curIn.end)
            while curMeetings and curMeetings[0] <= curIn.start:
                heapq.heappop(curMeetings)
            if len(curMeetings) > rs:
                rs = len(curMeetings)
        
        return rs