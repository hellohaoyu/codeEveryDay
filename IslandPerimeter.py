# Leetcode: https://leetcode.com/problems/island-perimeter/description/

# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
# and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" 
# (water inside that isn't connected to the water around the island). One cell is a square with side length 
# 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example:

# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rs = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
              rs += self. getIslandCellEdges(i, j, grid)
        
        return rs
    
    def getIslandCellEdges(self, x, y, grid):
        rs = 0
        if grid[x][y] == 0:
            return rs
        
        # check left:
        if y == 0 or  grid[x][y-1] == 0:
            rs += 1
        
        # check right:
        if y == (len(grid[0]) - 1) or grid[x][y+1] == 0:
            rs += 1 
        
        # check up:
        if x == 0 or  grid[x-1][y] == 0:
            rs += 1
        
        # check down:
        if x == (len(grid) - 1) or grid[x+1][y] == 0:
            rs += 1 
        
        return rs