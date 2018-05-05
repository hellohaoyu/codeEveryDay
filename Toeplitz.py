# Leetcode: https://leetcode.com/problems/toeplitz-matrix/description/

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: True
# Explanation:
# 1234
# 5123
# 9512


class Solution(object):
    OFFSET = [1,1]
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        maxX = len(matrix): # 2
        if maxX <= 1:
            return True
        maxY = len(maxtrix[0]) # 3
        if maxY <= 1:
            return True
        
        for x in xrange(maxX): # [0, 1]
            for y in xrange(maxY): # [0,1,2]
                newX = x + Self.OFFSET[0]
                newY = y + Self.OFFSET[1]
                if self.isValidCoordinate(newX, newY, matrix) and matrix[x][y] != matrix[newX][newY]: # 1==1
                    return False
        
        return True
        
    def isValidCoordinate(self, x, y, matrix):
        return x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
            
            
    # Better version:          
    # for(int i= 0; i < matrix.length-1; i++) {
    #     for(int j = 0; j < matrix[0].length-1; j++){
    #         if( matrix[i][j] != matrix[i+1][j+1]){
    #             return false;
    #         }
    #     }
    # }
    # return true;
    