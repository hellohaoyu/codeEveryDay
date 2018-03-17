# Leetcode Link: https://leetcode.com/problems/number-of-islands/description/

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:

# 11000
# 11000
# 00100
# 00011
# Answer: 3

# Keys: 1. Use mast points as constant
#       2. Never forget to check if position is land before running search
#       3. After checked an island position, remember to set it as water `0`.

class Solution(object):
    MASK_POINTS = [[1,0], [0,1], [0,-1], [-1,0]]
    rs = 0
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        self.rs = 0
        for x in xrange(len(grid)):
            for y in xrange(len(grid[0])):
                if grid[x][y] == '1':
                    self.rs += 1
                    self.checkIsland(x, y, grid)

        return self.rs

    def checkIsland(self, x, y, grid):
        grid[x][y] = '0' # visited
        for offSet in self.MASK_POINTS:
            newX = x + offSet[0]
            newY = y + offSet[1]
            if self.checkPointValid(newX, newY, grid) and grid[newX][newY] == '1':
                self.checkIsland(newX, newY, grid)
    
    def checkPointValid(self, x, y, grid):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])