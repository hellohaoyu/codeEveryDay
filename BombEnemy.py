# Leetcode: https://leetcode.com/problems/bomb-enemy/description/

# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.

# Example:
# For the given grid

# 0 E 0 0
# E 0 W E
# 0 E 0 0

# return 3. (Placing a bomb at (1,1) kills 3 enemies)

class Solution(object):
    DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        
        maxKilled = 0
        for x in xrange(row):
            for y in xrange(col):
                if grid[x][y] == '0':
                    maxKilled = max(maxKilled, self.getKilledEnemy(grid, x, y))
        
        return maxKilled
    
    def getKilledEnemy(self, grid, x, y):
        count = 0
        for move in self.DIRS:
            newX = x
            newY = y
            while self.isValid(newX, newY, grid) and grid[newX][newY] != 'W':
                if grid[newX][newY] == 'E':
                    count += 1
                newX += move[0]
                newY += move[1]
        return count
    
    def isValid(self, x, y, grid):
        return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])




# Better solution with O(mn) time and space
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        tempRs = []
        for i in xrange(row):
            rowList = [0] * col
            tempRs.append(rowList)
        
        self.init(grid, tempRs)
        
        maxRs = 0
        for x in xrange(row):
            for y in xrange(col):
                if grid[x][y] == '0':  # Still need to check each postion and see if it's eligible for a bomb.
                    maxRs = max(maxRs, tempRs[x][y])
        
        return maxRs
        
    def init(self, grid, tempRs):
        row = len(grid)
        col = len(grid[0])
        
        for r in xrange(row):
            preC = 0
            c = 0
            count = 0
            while c < col:
                if grid[r][c] == 'E':
                    count += 1
                elif grid[r][c] == 'W':
                    for i in xrange(preC, c):
                        tempRs[r][i] += count
                    preC = c+1
                    count = 0
                c += 1
            for i in xrange(preC, col):  # Be careful to deal with the case without wall!!
                tempRs[r][i] += count
        
        for c in xrange(col):
            preR = 0
            r = 0
            count = 0
            while r < row:
                if grid[r][c] == 'E':
                    count += 1
                elif grid[r][c] == 'W':
                    for i in xrange(preR, r):
                        tempRs[i][c] += count
                    preR= r+1
                    count = 0
                r += 1
                
            for i in xrange(preR, row):
                tempRs[i][c] += count
