# Leetcode: https://leetcode.com/problems/game-of-life/description/

# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.

class Solution(object):
    OFF_SET =[[1,-1],[1,0],[1,1],[0,-1],[0,1],[-1,-1],[-1,0],[-1,1]]   # For the area issue, remember to use offset constant!!
    LIVE_TO_DIE = 2 # In-place solution is to define extra states!!
    LIVE_TO_LIVE = 1 
    DIE_TO_LIVE = 3
    DIE_TO_DIE = 0
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
            
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                board[x][y] = self.getNextState(board, x, y)
        
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                 board[x][y] %= 2 
    
    def getNextState(self, board, x, y):
        max_x = len(board)
        max_y = len(board[0])
        numLive = 0
        
        for offSet in self.OFF_SET:
            new_x = x + offSet[0]
            new_y = y + offSet[1]
            if self.checkPositionValid(max_x, max_y, new_x, new_y):
                if board[new_x][new_y] == self.LIVE_TO_LIVE or board[new_x][new_y] == self.LIVE_TO_DIE :
                    numLive += 1
        
        if board[x][y]:
            return self.LIVE_TO_LIVE if numLive == 2 or numLive == 3 else self.LIVE_TO_DIE  # remember there is no `true ? A: B`, remember to use  `A if true else B`
                
        return self.DIE_TO_LIVE if numLive == 3 else self.DIE_TO_DIE  
    
    def checkPositionValid(self, max_x, max_y, x, y):
        return x >= 0 and x < max_x and y >= 0 and y < max_y