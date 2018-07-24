# Leetcode: https://leetcode.com/problems/design-hit-counter/description/

# Design a hit counter which counts the number of hits received in the past 5 minutes.

# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

# It is possible that several hits arrive roughly at the same time.

# Example:
# HitCounter counter = new HitCounter();

# // hit at timestamp 1.
# counter.hit(1);

# // hit at timestamp 2.
# counter.hit(2);

# // hit at timestamp 3.
# counter.hit(3);

# // get hits at timestamp 4, should return 3.
# counter.getHits(4);

# // hit at timestamp 300.
# counter.hit(300);

# // get hits at timestamp 300, should return 4.
# counter.getHits(300);

# // get hits at timestamp 301, should return 3.
# counter.getHits(301); 
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?


# Key: 1. Think of using clear data method in getHits (Get accurate val) and hit(avoid counting duplicates)
#      2. THink of remembering the newest time, which could be used to get index!!


class HitCounter(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hitMap = [0] * 300
        self.newest = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.clearOutDated(timestamp)
        self.newest = timestamp
        self.hitMap[timestamp % 300] += 1
        
    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self.clearOutDated(timestamp)
        return sum(self.hitMap)
    
    def clearOutDated(self, timestamp):
        offSet = timestamp - self.newest
        for i in xrange(1, offSet + 1 if offSet < 300 else 301):
            self.hitMap[(self.newest + i) % 300] = 0