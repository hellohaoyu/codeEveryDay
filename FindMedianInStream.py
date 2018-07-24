# Leetcode: https://leetcode.com/problems/find-median-from-data-stream/description/

# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# For example,
# [2,3,4], the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# Example:

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2


# Key points: 1. Use two heaps and lower and upper heaps store the value differently 
# (upper part stores positive values while lower part stores negetive values, it will help to return the largest value from lowerpart) 

import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lowerHeap = []
        self.upperHeap = []
        heapq.heapify(self.lowerHeap)
        heapq.heapify(self.upperHeap)

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        popFromUpper = heapq.heappushpop(self.upperHeap, num)
        heapq.heappush(self.lowerHeap, -popFromUpper)  # Store negative values to lower part
        if len(self.lowerHeap) > len(self.upperHeap):
            heapq.heappush(self.upperHeap, -heapq.heappop(self.lowerHeap))
        
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.upperHeap) > len(self.lowerHeap):
            return float(self.upperHeap[0])
        return (self.upperHeap[0] - self.lowerHeap[0]) / 2.0