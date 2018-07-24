# Leetcode: https://leetcode.com/problems/range-addition/description/

# Assume you have an array of length n initialized with all 0's and are given k update operations.

# Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

# Return the modified array after all k operations were executed.

# Example:

# Given:

#     length = 5,
#     updates = [
#         [1,  3,  2],
#         [2,  4,  3],
#         [0,  2, -2]
#     ]

# Output:

#     [-2, 0, 3, 5, 3]
# Explanation:

# Initial state:
# [ 0, 0, 0, 0, 0 ]

# After applying operation [1, 3, 2]:
# [ 0, 2, 2, 2, 0 ]

# After applying operation [2, 4, 3]:
# [ 0, 2, 5, 5, 3 ]

# After applying operation [0, 2, -2]:
# [-2, 0, 3, 5, 3 ]

# The algorithm is genious!!!
# You have to have some observation:
# 1. Order doesn't matter
# 2. Cumulative sum is from multiple queries!

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        rs = [0] * length
        
        for update in updates:
            val = update[2]
            s = update[0]
            e = update[1]
            
            rs[s] += val
            if e < length - 1:
                rs[e+1] -= val
        
        for i in xrange(1, length):
            rs[i] += rs[i-1] 
        
        return rs