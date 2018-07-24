# Leetcode: https://leetcode.com/problems/number-of-corner-rectangles/description/

# Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

# A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.

 

# Example 1:

# Input: grid = 
# [[1, 0, 0, 1, 0],
#  [0, 0, 1, 0, 1],
#  [0, 0, 0, 1, 0],
#  [1, 0, 1, 0, 1]]
# Output: 1
# Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
 

# Example 2:

# Input: grid = 
# [[1, 1, 1],
#  [1, 1, 1],
#  [1, 1, 1]]
# Output: 9
# Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
 

# Example 3:

# Input: grid = 
# [[1, 1, 1, 1]]
# Output: 0
# Explanation: Rectangles must have four distinct corners.

# Key: Use dict with tuple to find the corrosponding value.

from collections import defaultdict
class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        maps = defaultdict(int)
        for row in grid:
            for s in xrange(len(row)):
                if row[s]:
                    for e in xrange(s+1, len(row)):
                        if row[e]:
                            ans += maps[(s, e)] # Find one pair then get the  number of combinations (Pre)
                            maps[(s, e)] += 1 # Add combinations!
        return ans