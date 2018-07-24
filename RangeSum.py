# Leetcode: https://leetcode.com/problems/range-sum-query-2d-immutable/description/

# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        self.sumMaps = [[0] * (cols+1) for i in xrange(rows+1)] # Has to be m+1 * n+1!!
        
        for r in xrange(1, rows+1):
            sumV = 0
            for c in xrange(1, cols+1): # Remember to have right index!!! 
                sumV += matrix[r-1][c-1]
                self.sumMaps[r][c] = sumV + (self.sumMaps[r-1][c] if r > 1 else 0) 
                
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sumMaps[row1][col1] + self.sumMaps[row2+1][col2+1] - self.sumMaps[row1][col2+1] - self.sumMaps[row2+1][col1]
