# Leetcode: https://leetcode.com/problems/spiral-matrix/

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


# For the matrix issue -> Please be really careful about what x and y represent!! Don't mix them wrongly!!

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rs = []
        if not matrix or not matrix[0]:
            return rs
        self.helper(matrix, 0, 0, len(matrix), len(matrix[0]), rs)
        
        return rs
    
    def helper(self, matrix, sx, sy, xMax, yMax, rs):
        if sx >= xMax or sy >= yMax:
            return
        
        # upper
        for y in xrange(sy, yMax):
            rs.append(matrix[sx][y])
        
        # right
        for x in xrange(sx+1, xMax): 
            rs.append(matrix[x][yMax-1])
        
        # bottom
        if sx < xMax - 1:
            for y in reversed(xrange(sy, yMax-1)):
                rs.append(matrix[xMax-1][y])

        # left
        if sy < yMax - 1:
            for x in reversed(xrange(sx+1, xMax-1)):
                rs.append(matrix[x][sy]) 
        
        self.helper(matrix, sx+1, sy+1, xMax - 1, yMax -1, rs)