
# Leetcode: https://leetcode.com/problems/daily-temperatures/discuss/

# Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

# Key: 1. Relize the limited range of temperatures
# 

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
# 1. Naive solution        
#         l = len(temperatures)
#         rs = [0] * l
        
#         for i in xrange(l-2, -1, -1):
#             for j in xrange(i+1, l):
#                 if temperatures[j] > temperatures[i]:
#                     rs[i] = j - i
#                     break
#         return rs

# Solution with limited range of temperatures.
        lower = 30
        upper = 100
        tRange = upper - lower + 1
        ranges = [0] * tRange
        rs = []
        for t in reversed(temperatures):
            rs.append(ranges[t - lower])
            for i in xrange(tRange):
                if ranges[i]:
                    ranges[i] += 1
            for i in xrange(t - lower):
                ranges[i] = 1
                
        return rs[::-1]


# Better solution by using previous result to accumulate result.
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        size = len(temperatures)
        rs = [0] * size
        
        for cur in xrange(size - 2, -1, -1):
            nextI = cur + 1
            if temperatures[nextI] > temperatures[cur]:
                rs[cur] = 1
            else:            
                while nextI < size and temperatures[nextI] <= temperatures[cur]:
                    if rs[nextI]:
                        nextI += rs[nextI]
                    else:
                        nextI = size  # remember to set nextI to the size when the val is zero under nextI.
                if nextI < size:
                    rs[cur] = nextI -  cur
        return rs