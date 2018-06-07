# Leetcode: https://leetcode.com/problems/diagonal-traverse/description/

# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]

class Solution(object):
    MOVES = [[-1, 1], [1, -1]]
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rs = []
        if not matrix or not matrix[0]:
            return rs
        m = len(matrix)
        n = len(matrix[0])
        rsSize = m*n
        rs = []
        direction = 0 # up
        
        curX = 0
        curY = 0
        
        for i in xrange(rsSize):
            print curX, curY
            rs.append(matrix[curX][curY])
            
            if (curX + curY) % 2 == 0: # Up
                if curX == 0: # It will give (0,3) -- out of bound result, instead of (1,2)
                    curY += 1
                elif curY == n - 1:
                    curX += 1
                else:
                    curY += 1
                    curX -= 1
            else:   # Down
                if curX == m - 1:
                    curY += 1
                elif curY == 0:
                    curX += 1
                else:
                    curY -= 1
                    curX += 1
        
        return rs
# print curX, curY => It will be out of boundary, because when we visited (0,2) corner point, we need to got to (1, 2) , instead of (0, 3). The code above will get error.       
# 0 0
# 0 1
# 1 0
# 2 0
# 1 1
# 0 2
# 0 3


class Solution(object):
    MOVES = [[-1, 1], [1, -1]]
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rs = []
        if not matrix or not matrix[0]:
            return rs
        m = len(matrix)
        n = len(matrix[0])
        rsSize = m*n
        rs = []
        direction = 0 # up
        
        curX = 0
        curY = 0
        
        for i in xrange(rsSize):
            print curX, curY
            rs.append(matrix[curX][curY])
            
            if (curX + curY) % 2 == 0: # When the sum of x,y is even, then we need to move up!! Good trick here!
                if curY == n - 1:  # When comeing across max index bound, it has higher priority.  
                    curX += 1
                elif curX == 0:
                    curY += 1
                else:
                    curY += 1
                    curX -= 1
            else:   # Down
                if curX == m - 1:
                    curY += 1
                elif curY == 0:
                    curX += 1
                else:
                    curY -= 1
                    curX += 1
        return rs